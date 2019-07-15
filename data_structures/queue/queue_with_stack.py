"""Queue implemented using pseudo stacks (represented by a list with pop and append)"""
class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def __str__(self):
        return str(self.stack2[::-1] + self.stack1)

    def put(self, item):
        self.stack1.append(item)

    def get(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop()) 
        return self.stack2.pop()

    def rotate(self, rotation):
        for i in range(0, rotation):
            self.put(self.get())

    def front(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop()) 
        return self.stack2[-1]

    def size(self):
        return len(self.stack1) + len(self.stack2)

if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.put(i)

    print('Initial queue: ' + str(queue))
    print('get(): ' + str(queue.get()))
    print('After get(), the queue is now: ' + str(queue))
    queue.put(100)
    print('After put(100), the queue is now: ' + str(queue))
    print('size(): ' + str(queue.size()))
    queue.rotate(3)
    print('After rotate(3), the queue is now: ' + str(queue))
