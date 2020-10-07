#------------
#Playfair Cipher
#------------

#imports
import sys

#variables
global mode, key, text

#functions

def process_inputs():
    if len(sys.argv) < 4:
        sys.exit()

    #args from command line
    mode = sys.argv[1]
    text = sys.argv[2]
    input_key = sys.argv[3]
    key = []

    #cut input into chunks of 5 characters
    nums_iterate = [0,5,10,15,20]
    for i in nums_iterate:
        key.append(input_key[i:i+5])
    print(key)

def insert_x(letter_pair):
    #
    print()

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

if __name__ == '__main__':
    process_inputs()
