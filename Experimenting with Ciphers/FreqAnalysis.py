LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def getLetterCount(message):
    # return a dictionary with the frequency of each letter appearance
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
                'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for char in message.upper():
        if char in LETTERS:
            letterCount[char] += 1
    return letterCount

def getItemAtIndexZero(items):
    return items[0]

def getFrequencyOrder(message):
    # return a string of arranged letters in ETAOIN oreder
    # by frequency of appearance

    letterToFreq = getLetterCount(message)

    # create a dict for each frequency count with its coresponding letters
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter] # create a key of that letter's frequency and its value
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    # sort each list of letters in freqToLetters in reverse ETAOIN order
    for freq in freqToLetter:
        freqToLetter[freq].sort(key = ETAOIN.find, reverse = True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    # convert freqToLetter into tuples list, and sort it by frequency
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key = getItemAtIndexZero, reverse = True)

    # create a list of all the strings of letters from the list of tuples
    freqOrder = []
    for pair in freqPairs:
        freqOrder.append(pair[1])
    
    # finally return the sorted string
    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    # return integer number of matches of 6 most frequent letters in english
    # and 6 least commont 
    freqOrder = getFrequencyOrder(message)

    matchScore = 0
    # check for first 6
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    # check for last 6
    for commonLetter in ETAOIN[-6:]:
        if commonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore


