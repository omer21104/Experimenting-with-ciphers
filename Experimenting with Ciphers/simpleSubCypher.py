import random, sys, pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    key = getRandomKey()

    myMessage = """If a man is offered a fact which goes against his           
    instincts, he will scrutinize it closely, and unless the evidence           
    is overwhelming, he will refuse to believe it. If, on the other           
    hand, he is offered something which affords a reason for acting           
    in accordance to his instincts, he will accept it even on the           
    slightest evidence. The origin of myths is explained in this way.           
    -Bertrand Russell"""

    
    if not validateKey(key):
        # chars in key dont match LETTERS, terminate
        sys.exit('Error with the key, terminating')

    print('Enter \'E\' to encrypt or \'D\' to decrypt:')
    response = input('> ')
    if response.strip().upper().startswith('E'):
        translatedText = encrypt(key, myMessage)
    elif response.strip().upper().startswith('D'):
        translatedText = decrypt(key, myMessage)

    print('Message: %s' % translatedText)
    print('key: %s' % key)
    pyperclip.copy(translatedText)



def validateKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList

def encrypt(key, message):
    return translateMessage(key, message, 'encrypt')

def decrypt(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    # same function to encrypt and decrypt
    translatedText = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA # switch roles
    
    # loop through each char in message, add to translatedText
    for char in message:
        if char.upper() in charsA:
            charIndex = charsA.find(char.upper())
            if char.isupper():
                translatedText += charsB[charIndex].upper()
            else:
                translatedText += charsB[charIndex].lower()
        else: # char not in the list just add it
            translatedText += char
    return translatedText

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()