# coding=utf-8
"""
用两个队列实现栈
"""


class TwoQueueStack(object):
    def __init__(self):
        self.queue = []
        self.help_queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if not self.queue:
            raise IndexError('the queue is empty')
        while len(self.queue) != 1:
            self.help_queue.append(self.queue.pop(0))
        result = self.queue.pop()
        self.queue, self.help_queue = self.help_queue, self.queue
        return result

    def peek(self):
        if not self.queue:
            raise IndexError('the queue is empty')
        while len(self.queue) != 1:
            self.help_queue.append(self.queue.pop(0))
        result = self.queue.pop()
        self.help_queue.append(result)
        self.queue, self.help_queue = self.help_queue, self.queue
        return result
