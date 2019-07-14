"""Queue represented by a list"""

class Queue():
    def __init__(self):
        self.queue = []
        self.front = 0

    def __str__(self):
        return str(self.queue)

    def put(self, item):
        self.queue.append(item)

    def get(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    """Rotates the queue {@code rotation} times
    @param rotation
        number of times to rotate queue"""
    def rotate(self, rotation):
        for i in range(0, rotation):
            self.put(self.get())

    def front(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

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
