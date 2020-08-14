import SimpleSubHacker, makeWordPatterns, wordPatterns, re

word1 = 'OLQIHXIRCKGNZ'
word2 = 'PLQRZKBZB'
word3 = 'MPBKSSIPLC'

words = ['OLQIHXIRCKGNZ','PLQRZKBZB','MPBKSSIPLC']
letterMap1 = SimpleSubHacker.getBlackCipherLetterMapping()
letterMap2 = SimpleSubHacker.getBlackCipherLetterMapping()
letterMap3 = SimpleSubHacker.getBlackCipherLetterMapping()

letterMaps = []
letterMaps.append(letterMap1)
letterMaps.append(letterMap2)
letterMaps.append(letterMap3)

wordPat1 = makeWordPatterns.getWordPattern(word1)
wordPat2 = makeWordPatterns.getWordPattern(word2)
wordPat3 = makeWordPatterns.getWordPattern(word3)

patterns = []
patterns.append(wordPat1)
patterns.append(wordPat2)
patterns.append(wordPat3)
print(patterns)

cands = []
for pattern in patterns:
    cands.append(wordPatterns.allPatterns[pattern])

print(cands)
for candidateList in cands:
    for candidate in candidateList:
        mapIndex = cands.index(candidateList)
        SimpleSubHacker.addLettersToMapping(letterMaps[mapIndex], words[mapIndex], candidate)
        
   

intersectedMapping = SimpleSubHacker.intersectMapping(letterMap1, letterMap2)
intersectedMapping = SimpleSubHacker.intersectMapping(intersectedMapping, letterMap3)
print(intersectedMapping)

foo = SimpleSubHacker.removeSolvedLetterFromMapping(intersectedMapping)
print(foo)

regi = re.compile('[^A-Z]\s')