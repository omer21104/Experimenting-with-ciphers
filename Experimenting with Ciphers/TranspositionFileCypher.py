import time, os, sys, Transposition

def main():
    inputFileName = 'frankenstein.encrypted.txt'
    # WATCH OUT FOR OVERRIDE IF OUTPUTFILENAME ALREADY EXISTS
    outputFileName = 'frankenstein.decrypted.txt'
    myKey = 10
    myMode = 'decrypt' # 'encrypt' / 'decrypt'

    # make sure inputFileName path exists
    if not os.path.exists(inputFileName):
        print('%s does not exist. Quitting...' % (inputFileName))
        sys.exit()

    # if the output file already exists give a chance to quit
    if os.path.exists(outputFileName):
        print('This will overwrite %s. (C)ontinue or (Q)uit?' % (outputFileName))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # read input file
    fileObject = open(inputFileName)
    content = fileObject.read()
    fileObject.close()

    print('%sing...' % (myMode.title()))
    # encrypt or decrypt
    # measure time
    startTime = time.time()
    if myMode == 'encrypt':
        translated = Transposition.encrypt(content, myKey)
    elif myMode == 'decrypt':
        translated = Transposition.decrypt(content, myKey)
    
    totalTime = round((time.time() - startTime) , 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # write output to a new file
    outputFileObject = open(outputFileName, 'w')
    outputFileObject.write(translated)
    outputFileObject.close()

    print('done %sing' % (myMode.title()))

if __name__ == '__main__':
    main()


