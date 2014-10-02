"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import *

def main():
    
    while True:
        our_input = raw_input('> ') 
        tokens = our_input.split(' ')
        if our_input == "q":
            break
        else:
            if tokens[0] == "pow":
                print power(int(tokens[1]), int(tokens[2]))
            if tokens[0] == "+":
                print add(int(tokens[1]), int(tokens[2]))
            if tokens[0] == "-":
                print subtract(int(tokens[1]), int(tokens[2]))
            if tokens[0] == "*":
                print multiply(int(tokens[1]), int(tokens[2]))
            if tokens[0] == "/":
                print divide(int(tokens[1]), int(tokens[2]))
            if tokens[0] == "square":
                print square(int(tokens[1]), int(tokens[2]))
            if tokens[0] == "cube":
                print cube(int(tokens[1]), int(tokens[2]))
            if tokens[0] == "mod":
                print modulus(int(tokens[1]), int(tokens[2]))




if __name__ == '__main__':
    main()




