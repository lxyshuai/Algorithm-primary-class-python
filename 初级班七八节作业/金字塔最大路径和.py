# coding=utf-8
"""
假设有如下所示的一个数字金字塔，
    7
   3 2
  8 1 0
 2 7 4 4
4 5 2 6 5
现在，要求写一个程序来查找从顶点到底部任意处结束的路径，使路径经过的数字的和最大，并输出该路径的最大和。
比如以下金字塔的和最大路径的和为7+3+8+7+5=30。
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def get_max_path_recursive_node(root):
    # basecase
    return process_node(root, sum)


def process_node(root, sum):
    left = process_node(root.left, sum) if root.left else 0
    right = process_node(root.right, sum) if root.right else 0
    sum = root.value + max(left, right)
    return sum


def get_max_path_recursive_array(array):
    # basecase
    return process_array(array, 0, 0)


def process_array(array, x, y):
    if not array:
        return
    if x == len(array) - 1:
        return array[x][y]
    left = process_array(array, x + 1, y)
    right = process_array(array, x + 1, y + 1)
    return max(left, right) + array[x][y]


def get_max_path_dp(array):
    dp_array = [[0 for _ in range(k + 1)] for k in range(len(array) + 1)]
    for i in dp_array[-1]:
        i = 0
    for x in reversed(range(len(dp_array) - 1)):
        for y in reversed(range(len(dp_array[x]))):
            dp_array[x][y] = max(dp_array[x + 1][y] + array[x][y], dp_array[x + 1][y + 1] + array[x][y])
    return dp_array[0][0]


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(5)
    root.right.right = Node(6)
    print get_max_path_recursive_node(root)
    array = [[1], [2, 3], [4, 5, 6]]
    print get_max_path_recursive_array(array)
    print get_max_path_dp(array)
