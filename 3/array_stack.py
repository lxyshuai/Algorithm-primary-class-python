# coding=utf8
"""
用数组实现stack
"""


class ArrayStack(object):
    def __init__(self, init_size):
        if init_size < 0:
            raise ValueError('wrong size')
        self.size = 0
        self.array = [0 for _ in range(init_size)]

    def peek(self):
        if self.size != 0:
            return self.array[self.size - 1]
        return None

    def push(self, value):
        if self.size == len(self.array):
            raise IndexError('the stack is full')
        self.array[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError('the stack is empty')
        self.size -= 1
        return self.array[self.size]


if __name__ == '__main__':
    stack = ArrayStack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.push(3)
