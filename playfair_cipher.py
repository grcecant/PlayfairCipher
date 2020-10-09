#------------
#Playfair Cipher
#------------

#imports
import sys

#functions
def process_inputs():
    if len(sys.argv) < 4:
        sys.exit()

    #args from command line
    global mode, text, key
    mode = sys.argv[1]
    text = sys.argv[2].upper()
    input_key = sys.argv[3]
    key = []

    #cut input into chunks of 5 characters
    nums_iterate = [0,5,10,15,20]
    for i in nums_iterate:
        temp = []
        for j in range(i, i+5):
            temp.append(input_key[j])
        key.append(temp)
    print(key)

def insert_x(letter_pair):
    if first == second:
        text.insert("X", i+1)

def which_encode(letter_pair):
    #
    print()

def vertical_encode(letter_pair):
    #
    print()

def horizontal_encode(letter_pair):
    #
    print()

def regular_encode(letter_pair):
    #
    print()

#the meaty encode function!
def playfair_cipher_encode():
    #iterate through in pairs
    for i in range(len(text)-1):
        current_pair = [text[i], text[i+1]]
        first = current_pair[0]
        second = current_pair[1]

        print(current_pair)
        for i in key:
            if first in i:

        print(key.index(first))

        #if letters are the same, insert an x between them
        if first == second:
            insert_x(current_pair)

        #if letters are on the same row, use the letters below them to replace


        #if letters are on the same column, use the letters to their right to replace them


        #if the letters are different, replace them with the letters on the same row, but in the column of the other letter



if __name__ == '__main__':
    process_inputs()
    playfair_cipher_encode()
    #if mode == "encode":
        #playfair_cipher_encode()
