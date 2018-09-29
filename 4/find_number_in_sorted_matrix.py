"""
在行列都排好序的矩阵中找数
【题目】
给定一个有N*M的整型矩阵matrix和一个整数K，matrix的每一行和每一
列都是排好序的。实现一个函数，判断K是否在matrix中。
例如：
0 1 2 5
2 3 4 7
4 4 4 8
5 7 7 9
如果K为7，返回true；如果K为6，返回false。
【要求】
时间复杂度为O(N+M)，额外空间复杂度为O(1)。
"""


def is_contains(matrix, number):
    row = 0
    col = len(matrix[0]) - 1 if row else 0

    while row <= len(matrix) - 1 and col >= 0:
        if number == matrix[row][col]:
            return True
        elif number < matrix[row][col]:
            col -= 1
        else:
            row += 1
    return False


if __name__ == '__main__':
    matrix = [[0, 1, 2, 5], [2, 3, 4, 7], [4, 4, 4, 8], [5, 7, 7, 9]]
    print(is_contains(matrix, 4))
