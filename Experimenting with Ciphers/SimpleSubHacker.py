import wordPatterns, sys, re, os, pyperclip, simpleSubCypher, copy, makeWordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLetterRegEx = re.compile('[^A-Z\s]')

def main():
    myMsg = """Bz e pex bu wzzycyd e zemr tobmo hwyu ehebxur obu           
    bxurbxmru, oy tbjj umcnrbxbgy br mjwuyja, exd nxjyuu roy yibdyxmy           
    bu wiyctoyjpbxh, oy tbjj cyznuy rw lyjbyiy br. Bz, wx roy wroyc           
    oexd, oy bu wzzycyd uwpyrobxh tobmo ezzwcdu e cyeuwx zwc emrbxh           
    bx emmwcdexmy rw obu bxurbxmru, oy tbjj emmysr br yiyx wx roy           
    ujbhoryur yibdyxmy. Roy wcbhbx wz parou bu yfsjebxyd bx robu tea.           
    -Lycrcexd Cnuuyjj"""

    # Determine the possible valid ciphertext translations:
    print('Hacking...')
    letterMapping = hackSimpleSub(myMsg)
    # Display the results to the user:
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original ciphertext:')
    print(myMsg)
    print()
    print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherLetterMapping(myMsg, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)



def getBlackCipherLetterMapping():
    return {
        'A': [],'B': [],'C': [],'D': [],'E': [],'F': [],'G': [],'H': [],'I': [],'J': [],
        'K': [],'L': [],'M': [],'N': [],'O': [],'P': [],'Q': [],'R': [],'S': [],'T': [],
        'U': [],'V': [],'W': [],'X': [],'Y': [],'Z': []
        }

def addLettersToMapping(letterMapping, cipherWord, candidate):
    # iterate through each letter in cipherword, append corresponding
    # letter in the same index in candidate to its map if not already there
    for i in range(len(cipherWord)):
        if candidate[i] not in letterMapping[cipherWord[i]]:
            letterMapping[cipherWord[i]].append(candidate[i])

def intersectMapping(mapA, mapB):
    # combine two letterMaps into a single one, where only
    # overlapping key-value pairs exist
    intersectedMap = getBlackCipherLetterMapping()

    for letter in LETTERS:
        # blank list mean all letters are possible
        if (mapA[letter] == []):
            intersectedMap[letter] = copy.deepcopy(mapB[letter])
        elif (mapB[letter] == []):
            intersectedMap[letter] = copy.deepcopy(mapA[letter])

        else:
            # loop through all the letter keys in mapA and append any overlap
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMap[letter].append(mappedLetter)
    return intersectedMap

def removeSolvedLetterFromMapping(letterMapping):
    # find letter keys which hold 1 value meaning its encryption is found
    loopAgain = True
    while loopAgain:
        # assume no more iterations required
        loopAgain = False   
        solvedLetters = []
        for cipherLetter in LETTERS:
            if len(letterMapping[cipherLetter]) == 1:
                solvedLetters.append(letterMapping[cipherLetter][0]) # add that value letter

        # next loop through the map and remove any letters already found in solvedLetters
        for cipherLetter in LETTERS:
            for letter in solvedLetters:
                if len(letterMapping[cipherLetter]) != 1 and letter in letterMapping[cipherLetter]:
                    # remove it
                    letterMapping[cipherLetter].remove(letter)
                if letterMapping[cipherLetter] == 1:
                    # new solved letter found
                    loopAgain = True
    return letterMapping

def hackSimpleSub(message):
    intersectedMap = getBlackCipherLetterMapping()
    cipherWordList = nonLetterRegEx.sub('',message.upper()).split()

    # loop through the list of cipher words
    for cipherWord in cipherWordList:
        candidateMap = getBlackCipherLetterMapping()
        wordPattern = makeWordPatterns.getWordPattern(cipherWord)
        # check that pattern in all the patterns
        if wordPattern not in wordPatterns.allPatterns:
            continue
        # add letters to the map
        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherWord, candidate)
        # intersect that map
        intersectedMap = intersectMapping(candidateMap, intersectedMap)
    
    return removeSolvedLetterFromMapping(intersectedMap)

def decryptWithCipherLetterMapping(cipherText, letterMapping):
    # return a string of the decrypted message
    # first create a placeholder key
    key = ['x'] * len(LETTERS)
    # find and replace any single letter key-values in letterMapping
    for cipherLetter in LETTERS:
        if len(letterMapping[cipherLetter]) == 1:
            letterIndex = LETTERS.find(letterMapping[cipherLetter][0])
            key[letterIndex] = cipherLetter
        else: # replace ambiguous letters with '_'
            cipherText = cipherText.replace(cipherLetter.lower(), '_')
            cipherText = cipherText.replace(cipherLetter.upper(), '_')
    
    key = ''.join(key)

    return simpleSubCypher.decrypt(key, cipherText)

if __name__ == '__main__':
    main()