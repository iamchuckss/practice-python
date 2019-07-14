
class Stack:
   def __init__(self):
      self.stack = []

   def is_empty(self):
      return len(self.stack) == 0

   def push(self, data):
       self.stack.append(data)

   def pop(self):
      if self.is_empty():
         return None
      else:
         return self.stack.pop()