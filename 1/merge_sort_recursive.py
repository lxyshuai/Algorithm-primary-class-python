# coding=utf-8

from typing import List


def merge(array, left, middle, right):
    """

    @param array:
    @type array: list[int]
    @param left:
    @type left:
    @param middle:
    @type middle:
    @param right:
    @type right:
    @return:
    @rtype: int
    """
    help = []
    position_left = left
    position_right = middle + 1
    while position_left <= middle and position_right <= right:
        if array[position_left] < array[position_right]:
            help.append(array[position_left])
            position_left += 1
        else:
            help.append(array[position_right])
            position_right += 1
    if position_left <= middle:
        help.extend(array[position_left:middle + 1])
    if position_right <= right:
        help.extend(array[position_right:right + 1])

    array[left:right + 1] = help


def merge_sort_process(array, left, right):
    if left == right:
        return
    middle = left + (right - left) / 2
    merge_sort_process(array, left, middle)
    merge_sort_process(array, middle + 1, right)
    merge(array, left, middle, right)


def merge_sort(array):
    """
    归并排序主方法
    Args:
        array:

    Returns:

    """
    if not array:
        return
    merge_sort_process(array, 0, len(array) - 1)


if __name__ == '__main__':
    a = 1  # type: int
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]  # type: List[int]
    print(u"原列表为：%s" % alist)
    merge_sort(alist)
    print(u"新列表为：%s" % alist)
