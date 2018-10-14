# coding=utf-8
"""
给定一个字符串str，和一个整数k，返回str向右循环右移k位后的结
果(不用额外空间)
"""


def rotate_string(char_array, k):
    if not char_array:
        return char_array
    if k == 0:
        return char_array
    # 前半部分逆序
    reverse(char_array, 0, k - 1)
    # 后半部分逆序
    reverse(char_array, k, len(char_array) - 1)
    # 整体逆序
    reverse(char_array, 0, len(char_array) - 1)


def reverse(char_array, begin, end):
    while begin < end:
        char_array[begin], char_array[end] = char_array[end], char_array[begin]
        begin += 1
        end-=1

if __name__ == '__main__':
    char_array = range(5)
    rotate_string(char_array, 2)
    print char_array
