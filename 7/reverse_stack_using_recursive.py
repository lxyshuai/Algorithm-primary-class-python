# coding=utf-8
"""
给你一个栈，请你逆序这个栈，不能申请额外的数据结构，只能
使用递归函数。如何实现？
"""

def reverse(stack):
    if not stack:
        return
    bottom = get_and_remove_last_element(stack)
    reverse(stack)
    stack.append(bottom)

def get_and_remove_last_element(stack):
    result = stack.pop()
    if not stack:
        return result
    else:
        last = get_and_remove_last_element(stack)
        stack.append(result)
        return last

if __name__ == '__main__':
    stack = [1,2,3]
    reverse(stack)
    print stack