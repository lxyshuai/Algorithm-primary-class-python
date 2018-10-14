# coding=utf-8
"""
给定一个数组arr，返回所有子数组的累加和中，最大的累加和
"""
import sys


def max_sum(array):
    current_sum = 0
    max_sum = -sys.maxint
    for i in array:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum

if __name__ == '__main__':
    print max_sum([1,3,-3,5,-5,5])
