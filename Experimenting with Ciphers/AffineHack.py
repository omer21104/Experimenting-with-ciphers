import affineCypher, DetectEnglish, cryptomath, pyperclip

SILENT_MODE = False

def main():
    myMsg = """tvfZ8I4G!ovVZ4KOvO!X!om!vGZvw!vf.KK!Ov0qG!KK0d!qGvvvvvvvvvvv
        vvvv0uv0GvfZ4KOvO!f!0m!v.vM48.qv0qGZvw!K0!m0qdvGM.Gv0GvV.XvM48.q "vvvvvvvvvvv
        vvvv-tK.qv14o0qd"""

    hackedMsg = hack(myMsg)

    if hackedMsg != None:
        print(hackedMsg)
        print('copied to clipboard!')
        pyperclip.copy(hackedMsg)
    else:
        print('unable to hack')

def hack(message):
    print('hacking...')

    # range of possible keys for affine cypher is len(set size) ^ 2
    for key in range(len(affineCypher.SYMBOLS) ** 2):
        keyA = affineCypher.getKeyParts(key)[0]
        # keyA must satisfy gcd(keyA, len(set size)) == 1
        if cryptomath.gcd(keyA, len(affineCypher.SYMBOLS)) != 1:
            continue # skip current key if gcd isnt 1

        decryptedText = affineCypher.decrypt(key, message)
        if not SILENT_MODE:
            print('tried key: %s' % key)
            print('text: %s...' % decryptedText)

        if DetectEnglish.isEnglish(decryptedText):
            print('Found possible hack')
            print('Key: %s' % key)
            print('Message: %s' % decryptedText)
            print()
            print('Enter D for done, or just press Enter to continue hacking:')            
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()