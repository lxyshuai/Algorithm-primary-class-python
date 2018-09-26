# coding=utf8
"""
实现一个特殊的栈,在实现栈的基本功能的基础上,在实现返回栈中最小元素的操作
"""


class GetMinStack(object):
    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, value):
        self.data_stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        elif value < self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.data_stack:
            raise IndexError('the stack is empty')
        self.min_stack.pop()
        return self.data_stack.pop()

    def get_min(self):
        return self.min_stack[-1]


if __name__ == '__main__':
    min_stack = GetMinStack()
    min_stack.push(0)
    min_stack.push(2)
    min_stack.push(3)
    min_stack.push(1)
    min_stack.push(-1)
    print min_stack.get_min()
