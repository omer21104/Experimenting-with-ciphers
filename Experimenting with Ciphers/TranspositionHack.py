import Transposition, DetectEnglish, random, pyperclip

testMessage = """I am already far north of London, and as I walk in the streets of
Petersburgh, I feel a cold northern breeze play upon my cheeks, which
braces my nerves and fills me with delight.  Do you understand this
feeling?"""

    # encrypt testMsg with unknown key
def main():
    encryptedMsg = Transposition.encrypt(testMessage, random.randint(1, len(testMessage)))

    hackedMessage = hackTransposition(encryptedMsg)

    if hackedMessage == None:
        print('failed to hack')
    else:
        print('copying to clipboard: ')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)


def hackTransposition(message):
    for key in range(1, len(message)):
        hackAttempt = Transposition.decrypt(message, key)
        print('Trying key: %s' % key)
        if DetectEnglish.isEnglish(hackAttempt):
            # possible hack, confirm with user
            print()
            print('possible hack found:')
            print('key: %s, message: %s...' % (key, hackAttempt[:300]))
            print()
            print('enter C to confirm or any other key to keep trying')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return hackAttempt
    
    return None

if __name__ == '__main__':
    main()
