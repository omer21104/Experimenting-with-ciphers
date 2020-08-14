import os

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = ALPHABET + ALPHABET.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('CrackingCodesFiles\\dictionary.txt')
    englishWords = {}

    # create an array of all the words in dictionaryFile
    wordsArr = dictionaryFile.read().split('\n')
    # create a key in englishWords for each word, with None as value
    for word in wordsArr:
        englishWords[word] = None

    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    # make sure possibleWords isnt empty

    # count matches
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
  
    if possibleWords == []:
        return 0.0
    # return percentage [0.0, 1.0] of matches in message
    return float (matches) / len(possibleWords)

def removeNonLetters(message):
    letterFree = []
    for char in message:
        if char in LETTERS_AND_SPACE:
            letterFree.append(char)
    # return letterFree as a string
    return ''.join(letterFree)

def isEnglish(message, wordPercentage=60, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and 49.     
    # 85% of all the characters in the message must be letters or spaces 50.     
    # (not punctuation or numbers).
    if message == '':
        return False
    # calculate word matches in %
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    # calculate letters percentage (total chars without punctuation)
    numLetters = len(removeNonLetters(message))
    messageLettersPercent = float (numLetters) / len(message) * 100
    lettersMatch = messageLettersPercent >= letterPercentage

    return wordsMatch and lettersMatch
