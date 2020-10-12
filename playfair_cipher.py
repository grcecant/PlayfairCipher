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

    #print the key as a square
    print("The key is: ")
    for i in key:
        print(i)
    print('\n')

    #change all Js to Is
    for i in text:
        if i == "J":
            i = "I"

def insert_x(letter_pair, index):
    global encoded, text
    #shift the second letter of the pair down one
    new_text = text[:index] + second + text[index:]
    #reassign the value, because strings are immutable
    text = new_text


def which_encode(letter_pair):
    global first_row, first_col, second_row, second_col
    for i in key:
        if first in i:
            first_row = key.index(i)
            first_col = i.index(first)
        if second in i:
            second_row = key.index(i)
            second_col = i.index(second)
    print (first_row)
    print(second_row)
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

    #new row = one row lower
    new_first_row = (first_row + 1) % 5
    new_second_row = (second_row + 1) % 5

    #add key-retrieved letters to the final encoded string
    global encoded
    encoded += key[new_first_row][first_col]
    encoded += key[new_second_row][second_col]

    print("vertical encode")

def horizontal_encode(letter_pair):
    #encode:
    #if letters are on the same column, use the letters to their right to replace them

    #new column = one column to the right
    new_first_col = (first_col + 1) % 5
    new_second_col = (second_col + 1) % 5

    #add key-retrieved letters to the final encoded string
    global encoded
    encoded += key[first_row][new_first_col]
    encoded += key[second_row][new_second_col]

    print("horizontal encode")

def regular_encode(letter_pair):
    #encode:
    #if the letters are different, replace them with the letters on the same row, but in the column of the other letter
    global first_col, second_col
    #copy the first col value
    copy_first_col = first_col

    #swap the rows and columns
    first_col = second_col
    second_col = copy_first_col

    #add key-retrieved letters to final encoded string
    global encoded
    encoded += key[first_row][first_col]
    encoded += key[second_row][second_col]

    print("reg encode")


#the meaty encode function!
def playfair_cipher_encode():

    global encoded;
    encoded = ""
    current = 0
    end_of_text = len(text) - 1

    #iterate through in pairs
    while current < end_of_text:
        if current%2 == 0:
            current_pair = [text[current], text[current+1]]
            global first, second
            first = current_pair[0]
            second = current_pair[1]

            print(current_pair)

            #if letters are the same, insert an x between them
            if first == second:
                insert_x(current_pair, current)
                current_pair = [text[current], 'X']
                second = current_pair[1]
                end_of_text +=1

            #determine which function to use
            which_encode(current_pair)
        current+=1


if __name__ == '__main__':
    process_inputs()
    if mode == "encode":
        playfair_cipher_encode()
    print(encoded)
