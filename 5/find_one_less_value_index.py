# coding=utf-8
from __future__ import division

"""
在数组中找到一个局部最小的位置
【题目】
定义局部最小的概念。arr长度为1时，arr[0]是局部最小。arr的长度为
N(N>1)时，如果arr[0]<arr[1]，那么arr[0]是局部最小；如果arr[N-
1]<arr[N-2]，那么arr[N-1]是局部最小；如果0<i<N-1，既有
arr[i]<arr[i-1]，又有arr[i]<arr[i+1]，那么arr[i]是局部最小。
给定无序数组arr，已知arr中任意两个相邻的数都不相等。写一个函数，
只需返回arr中任意一个局部最小出现的位置即可。
不一定只有有序才能二分,只要区分出左右状态
"""


def get_less_index(array):
    if not array:
        return None
    if len(array) == 1:
        return 0
    # 第一种情况,最左边为局部最小
    if array[0] < array[1]:
        return 0
    # 第二种情况,最右边为局部最小
    if array[-1] < array[-2]:
        return len(array) - 1
    # 第三种情况,最左边最右边的趋势都是往中间凹陷,所以中间必定存在局部最小
    left = 1
    right = len(array) - 2
    while left < right:
        middle = left + (right - left) // 2
        if array[middle - 1] < array[middle]:
            right = middle - 1
        elif array[middle] > array[middle + 1]:
            left = middle + 1
        else:
            return middle
    return left


if __name__ == '__main__':
    array = [6, 5, 3, 4, 6, 7, 8]
    print get_less_index(array)
