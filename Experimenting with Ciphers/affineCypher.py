import sys, cryptomath, pyperclip, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
MODE = 'decrypt'

def main():
    myMsg = """"A computer would deserve to be called intelligent           
    if it could deceive a human into believing that it was human."           
    -Alan Turing"""

    encMsg = """"tvfZ8I4G!ovVZ4KOvO!X!om!vGZvw!vf.KK!Ov0qG!KK0d!qGvvvvvvvvvvv
vvvv0uv0GvfZ4KOvO!f!0m!v.vM48.qv0qGZvw!K0!m0qdvGM.Gv0GvV.XvM48.q "vvvvvvvvvvv
vvvv-tK.qv14o0qd"""

    encKey = 3279

    myKey = getRandomKey()
    
    # call encrypt or decrypt functions
    if MODE == 'encrypt':
        text = encrypt(myKey, myMsg)
    if MODE == 'decrypt':
        text = decrypt(encKey, encMsg)

    print('key : %s' % myKey)
    print('%sed text:' % MODE.title())
    print(text)
    print('copied to clipboard!')
    pyperclip.copy(text)





def getKeyParts (key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKeys(keyA, keyB):
    # verify keys
    if keyA == 1 and (MODE == 'encrypt'):
        sys.exit('KeyA is weak, choose a different key.')
        
    if keyB == 0 and (MODE == 'encrypt'):
        sys.exit('KeyB is weak, choose a different key.')

    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))

    # make sure keyA and set size are co-prime
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA , len(SYMBOLS)))

def encrypt(key, message):
    # get key parts
    keyA, keyB = getKeyParts(key)
    # validate key parts
    checkKeys(keyA,keyB)

    # proceed if checks passed
    cypherText = ''
    # multiply each char index by keyA, then add keyB finally % len(set size)
    for char in message:
        if char in SYMBOLS:
            # encrypt char
            charIndex = SYMBOLS.find(char)
            cypherText += SYMBOLS[(charIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            cypherText += char # add without encrypting
    
    return cypherText

def decrypt(key, message):
    # get key parts and verify them
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB)

    decryptedMsg = ''
    # get mod inverse of keyA
    modInverseA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    # to decrypt, subtract keyB index then multiply by modInverse of keyA and len(set size) 
    # and then % len(set size)
    for char in message:
        if char in SYMBOLS:
            charIndex = SYMBOLS.find(char)
            decryptedMsg += SYMBOLS[((charIndex - keyB) * modInverseA) % len(SYMBOLS)]
        else:
            decryptedMsg += char
    return decryptedMsg

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        # check co-prime
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

if __name__ == '__main__':
    main()



        
    