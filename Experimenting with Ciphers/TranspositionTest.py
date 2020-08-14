import random, sys, Transposition
def main():

    random.seed(42)
    tests = 20
    for i in range(tests):
        # generate a random string
        randLen = random.randint(4, 40)
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * randLen


        # convert message to a list and shuffle it
        message = list(message)
        random.shuffle(message)
        # convert back to string
        message = ''.join(message)

        print ('test %s: "%s..."' % (i + 1, message[:50]))
        print ('message length: %s' % (len(message)))

        # check all possible keys for each message
        for key in range (1, int (len(message) / 2)):
            encrypted = Transposition.encrypt(message, key)
            decrypted = Transposition.decrypt(encrypted, key)

            if (message != decrypted):
                print ("ERROR: mismatch with key: %s and message %s" % (key, message))
                print ("Decrypted as: %s" % (decrypted))
                sys.exit()

    # if we exit the loop the check completed
    print("Success.")

if __name__ == '__main__':
    print("running from main")
    main()