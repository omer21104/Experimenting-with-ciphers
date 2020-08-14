import VigenereCipher, pyperclip, FreqAnalysis, DetectEnglish
import re, itertools

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX_KEY_LENGTH = 16
NUM_MOST_FREQ_LETTERS = 4
SILENT_MODE = False
NONLETTERS_PATTERN = re.compile('[^A-Z]')

def main():
    ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""
    hackedMessage = hackVigenere(ciphertext)

    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')



def findRepeatSequencesSpacings(message):
    message = NONLETTERS_PATTERN.sub('', message.upper())

    # dict for sequence length and letters
    # keys are sequences and values are lists of int spacings
    seqSpacings = {}
    for seqLen in range(3,6):
        for seqStart in range(len(message) - seqLen):
            seq = message[seqStart:seqStart + seqLen]
            # seq starts from message[0:seqLen] and holds all sequences
            # next check for matches in the message
            for i in range(seqLen + seqStart, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    # found a repeated sequence
                    if seq not in seqSpacings:
                        seqSpacings[seq] = [] # init. a blank list
                    # append the length of that sequence to the list
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings

def getUsefulFactors(num):
    # Returns a list of useful factors of num. By "useful" we mean factors
    # less than MAX_KEY_LENGTH + 1 and not 1. For example,
    # getUsefulFactors(144) returns [2, 3, 4, 6, 8, 9, 12, 16].
    if num < 2:
        return []

    factors = []
    for i in range(2, MAX_KEY_LENGTH): # 1 isnt useful
        if num % i == 0:
            factors.append(i)
            otherFactor = int(num / i)
            if otherFactor < MAX_KEY_LENGTH and otherFactor != 1:
                factors.append(otherFactor)
    return list(set(factors)) # remove duplicate factors

def getItemAtIndexOne(x):
    return x[1]

def getMostCommonFactors(seqFactors):
    # First, get a count of how many times a factor occurs in seqFactors:
    factorCounts = {} # Key is a factor; value is how often it occurs.  
    
    for seq in seqFactors:
        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] = 0
            factorCounts[factor] += 1
    
    factorsByCount = []
    for factor in factorCounts:
        # exclude factors larger that MAX_KEY_LENGTH
        if factor <= MAX_KEY_LENGTH:
            # append a tuple of (factor, factorCount)
            factorsByCount.append( (factor, factorCounts[factor]) )
    
    factorsByCount.sort(key = getItemAtIndexOne, reverse = True)
    return factorsByCount

def kasiskiExamination(cipherText):
    # this function finds all the factors for each sequence
    # found with findRepeatSequencesSpacings and returns a list
    # of most likely factors to be key lengths
    repeatedSeqSpacings = findRepeatSequencesSpacings(cipherText)

    # get the most common factors
    seqFactors = {}
    for seq in repeatedSeqSpacings:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacings[seq]:
            seqFactors[seq].extend(getUsefulFactors(spacing))
    
    factorsByCount = getMostCommonFactors(seqFactors)
    # extract only the factors from factorsByCount
    # i.e get the first item of all the tuples of that list of tuples

    allLikelyFactors = []
    for twoItemTup in factorsByCount:
        allLikelyFactors.append(twoItemTup[0])
    
    return allLikelyFactors

def getNthSubkeysLetters (nth, keyLength, message):
    message = NONLETTERS_PATTERN.sub('', message)

    i = nth - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return ''.join(letters)

def attemptHackWithKeyLength(cipherText, mostLikelyKeyLength):
    # make a copy of cipherText in uppercase
    cipherTextUp = cipherText.upper()

    allFreqScores = []
    for nth in range(1, mostLikelyKeyLength + 1): # range(x,y) includes x; excludes y
        nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, cipherTextUp)

    # freqScores is a list of tuples like
    # [(<letter>, <Eng. Freq. match score>), ... ]
    # List is sorted by match score. Higher score means better match.
        freqScores = []
        for possibleKey in LETTERS:
            decryptedText = VigenereCipher.decrypt(nthLetters, possibleKey)
            keyAndFreqTuple = (possibleKey, FreqAnalysis.englishFreqMatchScore(decryptedText))
            # add that tuple to freqScores
            freqScores.append(keyAndFreqTuple)
        # sort freqScores in decending order (most frequent)
        freqScores.sort(key = getItemAtIndexOne, reverse = True)
        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])
    
    if not SILENT_MODE:
        for i in range(len(allFreqScores)):
            print('Possible letters for letter %s of the key: ' % (i + 1), end = '')
            for freqScore in allFreqScores[i]:
                print('%s ' % freqScore[0], end = '')
                print()

    # Try every combination of the most likely letters for each position
    # in the key:
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
        # create possible key from the letters in allFreqScores:
        possibleKey = ''
        for i in range(mostLikelyKeyLength):
            possibleKey += allFreqScores[i][indexes[i]][0]
        
        if not SILENT_MODE:
            print('attempting with key: %s' % (possibleKey))
        
        decryptedText = VigenereCipher.decrypt(cipherTextUp,possibleKey)

        if DetectEnglish.isEnglish(decryptedText):
            origCase = []
            for i in range(len(cipherText)):
                if cipherText[i].isupper():
                    origCase.append(decryptedText[i].upper())
                else:
                    origCase.append(decryptedText[i].lower())
            decryptedText = ''.join(origCase)

            # Check with user to see if the key has been found:
            print('Possible encryption hack with key %s:' % (possibleKey))
            print(decryptedText[:200]) # Only show first 200 characters.
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

 # No English-looking decryption found, so return None:
    return None
    
def hackVigenere(cipherText):
    allLikelyKeyLengths = kasiskiExamination(cipherText)
    
    if not SILENT_MODE:
        keyLengthStr = ''
        for keyLength in allLikelyKeyLengths:
            keyLengthStr += '%s ' % keyLength
        print('kasiski exam results says most likely key lengths are : ' + keyLengthStr + '\n')

    hackedMessage = None
    for keyLength in allLikelyKeyLengths:
        if not SILENT_MODE:
            print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
        hackedMessage = attemptHackWithKeyLength(cipherText, keyLength)
        if hackedMessage != None:
            break

        # If none of the key lengths found using Kasiski examination
        # worked, start brute-forcing through key lengths:
        if hackedMessage == None:
            if not SILENT_MODE:
                print('Unable to hack message with likely key length(s). Bruteforcingkey length...')
            for keyLength in range(1, MAX_KEY_LENGTH + 1):
                # no need to recheck lengths already tried from kasiski
                if keyLength not in allLikelyKeyLengths:
                    if not SILENT_MODE:
                        print('Attempting hack with key length %s (%s possiblekeys)...' % (keyLength, NUM_MOST_FREQ_LETTERS **keyLength))
                    hackedMessage = attemptHackWithKeyLength(cipherText, keyLength)
                    if hackedMessage != None:
                        break
    return hackedMessage

if __name__ == '__main__':
    main()