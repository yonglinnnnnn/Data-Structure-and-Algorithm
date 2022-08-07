# question 6
# note: a user can indicate end of input by typing ctrl-D
# hint: need to use the try and except blocks to capture the exception.
# hint: use a list to store all the lines then try using the built-in reverse() function to reverse the order
import sys


def invertedlist(input_list):
    input_list.reverse()
    return input_list

try:
    inputted_list = []
    while True:
        user_input = input('Enter a line (ctrl-D to stop): ')
        inputted_list.append(user_input)
except EOFError:
    # for normal sequence
    # for i in inputted_list:
    #     print(i)
    # print()

    # for reverse sequence
    words = invertedlist(inputted_list)
    for word in words:
        print(word)
