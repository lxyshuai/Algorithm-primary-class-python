# coding=utf8
"""
用数组实现queue
"""


class ArrayQueue(object):
    def __init__(self, init_size):
        if init_size < 0:
            raise ValueError('wrong size')
        self.size = 0
        self.first = 0
        self.last = 0
        self.array = [0 for _ in range(init_size)]

    def peek(self):
        if self.size == 0:
            return None
        return self.array[self.first]

    def push(self, value):
        if self.size == len(self.array):
            raise IndexError('the queue is full')
        self.size += 1
        self.array[self.last] = value
        self.last = self.last + 1 if self.last != len(self.array) - 1 else 0

    def poll(self):
        if self.size == 0:
            raise IndexError('the queue is empty')
        self.size -= 1
        temp = self.first
        self.first = self.first + 1 if self.first != len(self.array) - 1 else 0
        return self.array[temp]


if __name__ == '__main__':
    queue = ArrayQueue(5)
    queue.push(1)
    queue.push(2)
    print queue.poll()
