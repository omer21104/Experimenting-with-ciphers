import pyperclip, random
# this cipher works like caeser cipher, only uses a key which consists of subkeys
# key 'PIZZA' would encrypt first letter with key 'P' second with 'I' and so on.

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    key = 'OBJECTIONABLE'
    message = """On my computer, using string concatenation to build
10,000 strings that are 10,000 characters each took about 40 seconds, but
using the list-append-join process to do the same task took only 10 seconds.
If your program builds a lot of strings, using lists can make your program
much faster.
We’ll use"""

    print('select mode')
    print('\'E\' for encryption or \'D\' for decryption')
    response = input('> ')
    if response.strip().upper() == 'E':
        translated = encrypt(message, key)
        print(translated)
        print('encryting with key: %s' % key)
        pyperclip.copy(translated)
    elif response.strip().upper() == 'D':
        translated = decrypt(message,key)
        print(translated)
        pyperclip.copy(translated)

def getRandomKey():
    # 12 letters long is secure enough
    key = []
    for i in range(12):
        randomIndex = random.randint(0,len(LETTERS) - 1)
        key.append(LETTERS[randomIndex])
    return ''.join(key)
def encrypt(message, key):
    return translateMessage(message,key,'encrypt')

    
def decrypt(message, key):
    return translateMessage(message,key,'decrypt')

def translateMessage (message, key, mode):
    translatedMsg = []
    keyIndex = 0

    for char in message:
        charIndex = LETTERS.find(char.upper())
        currentKeyIndex = LETTERS.find(key[keyIndex])
        if charIndex != -1: # char was found in letters
            if mode == 'encrypt':
                # add charindex to current subkey index in letters
                # and append that to translated message
                charIndex += currentKeyIndex
                charIndex %= len(LETTERS)
                
            elif mode == 'decrypt':
                charIndex -= currentKeyIndex
                charIndex %= len(LETTERS)
                
           
            if char.isupper():
                translatedMsg.append(LETTERS[charIndex])
            else:
                translatedMsg.append(LETTERS[charIndex].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translatedMsg.append(char) # char not in letters
    return ''.join(translatedMsg)

if __name__ == '__main__':
    main()