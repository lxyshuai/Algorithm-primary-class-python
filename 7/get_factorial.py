# coding=utf-8
"""
求n!的结果
"""
def get_factorial(n):
    if n == 1:
        return 1
    return n * get_factorial(n - 1)
