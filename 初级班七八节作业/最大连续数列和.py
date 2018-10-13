# coding=utf-8
"""
对于一个有正有负的整数数组，请找出总和最大的连续数列。

给定一个int数组A和数组大小n，请返回最大的连续数列的和。保证n的大小小于等于3000。

测试样例：
[1,2,3,-6,1]
返回：6
"""

# -*- coding:utf-8 -*-
import sys


class MaxSum:
    def getMaxSum(self, A, n):
        if not A:
            return
        slow_index = 0
        fast_index = 0
        max_sum = -sys.maxint
        sum = 0
        while fast_index < n:
            sum += A[fast_index]
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                slow_index = fast_index + 1
                sum = 0
            fast_index += 1
        return max_sum

if __name__ == '__main__':
    a =MaxSum()
    a.getMaxSum([-1],1)