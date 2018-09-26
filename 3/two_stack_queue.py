# coding=utf-8
"""
用两个栈实现队列
"""


class TwoStacksQueue(object):
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, value):
        self.push_stack.append(value)

    def poll(self):
        if not self.push_stack and not self.pop_stack:
            raise IndexError('the stack is empty')
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        if not self.push_stack and not self.pop_stack:
            raise IndexError('the stack is empty')
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]
