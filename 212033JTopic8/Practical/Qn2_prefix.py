# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# this file consist of 1 (+ 2 from the Qn2.py) enhancement:
# 1. handle all the operations IN PREFIX FORM

from Qn1 import Stack

while True:
    expression = input("\nEnter a Postfix expression to be evaluated: ")
    tokens = expression.split(" ")  # Split the expression into individual tokens

    # separated by space
    myStack = Stack()  # Create an instance of the Stack object

    # Handle help option
    if tokens[0] == "help" or tokens[0] == "?":
        print(
            'Postfix Expression Evaluator takes in a mathematical expression expressed in Postfix notation and evaluates it.')
        print('Example: \"1 2 + 4 *\" will evaluate to \"12\"')
    # Handle quit option
    elif tokens[0] == "quit" or tokens[0] == "q":
        break
    # Handle Postfix expression entered
    else:
        valid = True
        # iterate over the string in reverse order
        for i in tokens[::-1]:
            # Handle operand
            if i.isdigit():
                myStack.push(float(i))
                myStack.peek()

            else:
                # pop value from stack to calc the result
                # push the result onto the stack again
                if len(myStack) >= 2:
                    o1 = myStack.pop()
                    o2 = myStack.pop()

                    # handle "+" operator
                    if i == "+":
                        myStack.push(o1+o2)
                    # handle "-" operator
                    elif i == '-':
                        # top - bottom value
                        myStack.push(o1 - o2)
                    # Handle "*" operator
                    elif i == '*':
                        myStack.push(o1 * o2)
                    # Handle "/" operator
                    elif i == '/':
                        # enhancement: handle 0 for division
                        if o2 > 0 or o2 < 0:
                            myStack.push(o1 / o2)
                        else:
                            print('Numbers cannot be divided by zero!')
                            valid = False
                            break
                    # Handle "^" operator
                    elif i == '^':
                        myStack.push(pow(o1, o2))
                    # enhancement: handle "%" operator
                    elif i == '%':
                        if o2 > 0 or o2 < 0:
                            myStack.push(o1 % o2)
                        else:
                            valid = False
                            break
                    # Any other characters are invalid
                    else:
                        valid = False
                        break

                else:
                    valid = False
                    break

        # For valid expression, there should only be one item left in the stack
        if len(myStack) != 1:
            valid = False

        # If expression is valid, print evaluation result
        # else print error message
        if valid:
            print('Evaluation Result: ', myStack.pop())
        else:
            print('Invalid Postfix expression!')


