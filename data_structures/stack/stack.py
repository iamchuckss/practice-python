from __future__ import print_function

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        # push an element to the top of the stack
        self.stack.append(data);

    def pop(self):
        # pop an element from the top of the stack
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('attempting to pop from empty stack')

    def peek(self):
        # peek at the top-most element of the stack
        if self.stack:
            return self.stack[-1];        
    
    def is_empty(self):
        # return not bool(self.stack)
        return len(self.stack) == 0
  
    def size(self):
        return len(self.stack)

if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print('Initial stack: ' + str(stack))
    print('pop(): ' + str(stack.pop()))
    print('After pop(), the stack is now: ' + str(stack))
    print('peek(): ' + str(stack.peek()))
    stack.push(100)
    print('After push(100), the stack is now: ' + str(stack))
    print('is_empty(): ' + str(stack.is_empty()))
    print('size(): ' + str(stack.size()))