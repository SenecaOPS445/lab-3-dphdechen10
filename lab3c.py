#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: 148596190

def operate(number1, number2, operator):
    if operator == "add":
        return number1 + number2
    elif operator == "subtract":
        return number1 - number2
    elif operator == "multiply":
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))