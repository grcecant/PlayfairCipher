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
    global first_row, first_col, second_row, second_col
    for i in key:
        if first in i:
            first_row = i
            first_col = i.index(first)
        if second in i:
            second_row = i
            second_col = i.index(second)
    #if on the same row, use vertical_encode
    if first_row == second_row:
        vertical_encode(letter_pair)
    #if same column, use horizontal_encode
    elif first_col == second_col:
        horizontal_encode(letter_pair)
    #if different, use regular encode
    else:
        regular_encode(letter_pair)


def vertical_encode(letter_pair):
    #encode:
    #if letters are on the same row, use the letters below them to replace
    print()

def horizontal_encode(letter_pair):
    #encode:
    #if letters are on the same column, use the letters to their right to replace them
    print()

def regular_encode(letter_pair):
    #encode:
    #if the letters are different, replace them with the letters on the same row, but in the column of the other letter

    print()

#the meaty encode function!
def playfair_cipher_encode():
    #iterate through in pairs
    for i in range(len(text)-1):
        current_pair = [text[i], text[i+1]]
        global first, second
        first = current_pair[0]
        second = current_pair[1]

        print(current_pair)

        #if letters are the same, insert an x between them
        if first == second:
            insert_x(current_pair)

        #if not on the same row, determine which function to use
        else:
            which_encode(current_pair)



if __name__ == '__main__':
    process_inputs()
    playfair_cipher_encode()
    #if mode == "encode":
        #playfair_cipher_encode()
