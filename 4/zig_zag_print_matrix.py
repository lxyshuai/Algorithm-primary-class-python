# coding=utf8
"""
“之”字形打印矩阵
【题目】
给定一个矩阵matrix，按照“之”字形的方式打印这个矩阵，例如：
1 2 3 4
5 6 7 8
9 10 11 12
“之”字形打印的结果为：1，2，5，9，6，3，4，7，10，11，8，12
【要求】
额外空间复杂度为O(1)。
"""


def print_diagonal(matrix, top_row, top_column, down_row, down_column, direction):
    """
    打印对角线
    @param matrix:
    @type matrix:
    @param top_row:
    @type top_row:
    @param top_column:
    @type top_column:
    @param down_row:
    @type down_row:
    @param down_column:
    @type down_column:
    @return:
    @rtype:
    """
    if direction:
        # 从上往下对角线遍历
        while top_row != down_row + 1 and top_column != down_column - 1:
            print matrix[top_row][top_column]
            top_row += 1
            top_column -= 1
    else:
        while down_row != top_row - 1 and down_column != top_column + 1:
            print matrix[down_row][down_column]
            down_row -= 1
            down_column += 1


def print_matrix_zig_zag(matrix):
    top_row = 0
    top_column = 0
    down_row = 0
    down_column = 0
    end_row = len(matrix) - 1
    end_column = len(matrix[0]) - 1 if end_row != 0 else 0
    direction = False
    while top_row != end_row + 1:
        print_diagonal(matrix, top_row, top_column, down_row, down_column, direction)
        top_row = top_row + 1 if top_column == end_column else top_row
        top_column = top_column if top_column == end_column else top_column + 1
        down_column = down_column + 1 if down_row == end_row else down_column
        down_row = down_row if down_row == end_row else down_row + 1
        direction = not direction


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix_zig_zag(matrix)
