from __future__ import print_function
from __future__ import absolute_import
from stack import Stack

def balanced_parentheses(string):
    """Check if the parentheses in a string is balanced by using a stack"""
    stack = Stack()
    for char in string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()

if __name__ == '__main__':
    string = ['((()))', '((())', '(()))']
    for char in string:
        print(char + ': ' + str(balanced_parentheses(char)))