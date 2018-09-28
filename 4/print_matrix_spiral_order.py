# coding=utf8
"""
转圈打印矩阵
【题目】
给定一个整型矩阵matrix，请按照转圈的方式打印它。
【要求】
额外空间复杂度为O(1)。
"""


def print_matrix_spiral_order(matrix):
    if not matrix:
        return
    top_row = 0
    top_column = 0
    down_row = len(matrix) - 1
    down_column = len(matrix[0]) - 1
    while top_column < down_column and top_row < down_row:
        print_edge(matrix, top_row, top_column, down_row, down_column)
        top_row += 1
        top_column += 1
        down_row -= 1
        down_column -= 1


def print_edge(matrix, top_row, top_column, down_row, down_column):
    # 两个点在同一行的情况
    if top_row == down_row:
        for _column in range(top_column, down_column + 1):
            print matrix[top_row][_column]
    # 两个点在同一列的情况
    elif top_column == down_column:
        for _row in range(top_row, down_column):
            print matrix[_row][top_column]
    # 两个点不在同一行且不再同一列
    else:
        current_row = top_row
        current_column = top_column
        # 上边
        while current_column < down_column:
            print matrix[top_row][current_column]
            current_column += 1
        # 右边
        while current_row < down_column:
            print matrix[current_row][down_column]
            current_row += 1
        # 下边
        while current_column > top_column:
            print matrix[down_row][current_column]
            current_column -= 1
        # 左边
        while current_row > top_row:
            print matrix[current_row][top_column]
            current_row -= 1


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix_spiral_order(matrix)
