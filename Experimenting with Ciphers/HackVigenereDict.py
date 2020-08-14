import DetectEnglish, pyperclip, VigenereCipher

def main():
    msg = """Co vc ehudhtfc, ygjwk umzwag dzrqbciptbwbn uz fijuh
10,000 umzwagt elou jvg 10,000 vpoeadeift neea bcbk bmsiu 40 biehvrf, bve
ygjwk vam zvsu-ltdfwh-lhqb crpnigt cs fh bvr sbxi hbbo vhwy bnmj 10 wsdxrfl.
Qt lovc tfppvcf jivled e zpc sh lbfvnhd, ygjwk nbahf cby qoln cqnz deohcea
ndgj yigges.
Hi’zm dwg"""
    hackedMsg = hack(msg)

    if hackedMsg != None:
        print('msg copied to clipboard')
        pyperclip.copy(hackedMsg)
    else:
        print('failed to hack')



def hack(message):
    foo = open('dictionary.txt')
    words = foo.readlines()
    foo.close()

    for word in words:
        word = word.strip() # remove newline chars

        decryptedText = VigenereCipher.decrypt(message, word)
        if DetectEnglish.isEnglish(decryptedText, wordPercentage=40):
            print('----')
            print('possible hack:')
            print('key: \'%s\' decrypted text: %s' % (str(word), decryptedText[:100]))
            print()
            print('Press C to confirm or any other key to keep hacking')
            response = input('> ')

            if response.upper().startswith('C'):
                return decryptedText

if __name__ == '__main__':
    main()