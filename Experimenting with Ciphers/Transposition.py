import math

def main():
    myMessage = "Omer is the king hahahahaha"
    key = 8

    encText = encrypt(myMessage, key)
    print(encText + '|')

    print(decrypt(encText,key))



def encrypt (message, key):
    # add chars from message to cypherList in 'key' steps
    cypherList = [''] * key

    for col in range(key):
        currentIndex = col

        while (currentIndex < len(message)):
            cypherList[col] += message[currentIndex]
            # increment index
            currentIndex += key

    return ''.join(cypherList)

def decrypt(message, key):
    # determine number of columns (ceil(message.length / key))
    # determine shaded boxes (colums * key - message.length)
    numberOfColumns = int (math.ceil(len(message) / key))
    numberOfRows = key
    shadedBoxes = numberOfColumns * key - len(message)

    # create a list for all the columns
    textList = [''] * numberOfColumns

    # add chars from the message to the columns of the list one by one
    col = 0
    row = 0

    for char in message:
        textList[col] += char
        col += 1

        # reset col to 0 if == to numberOfColumns
        # or col == numberOfColumns - 1 AND row == key - shadedBoxes
        if (col == numberOfColumns) or (col == numberOfColumns - 1 and row >= numberOfRows - shadedBoxes):
            col = 0
            row += 1

    return ''.join(textList)

if __name__ == "__main__":
    main()