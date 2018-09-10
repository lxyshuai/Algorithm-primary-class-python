# coding=utf-8
def selection_sort(array):
    """
    选择排序
    时间复杂度:O(N^2)
    额外空间复杂度:O(1)
    每轮将最小的值放在前面
    Args:
        array:

    Returns:

    """
    if not array:
        return
    for i in range(0, len(array) - 1):
        min_index = i
        for j in (i + 1, len(array) -1):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


if __name__ == '__main__':
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    selection_sort(alist)
    print("新列表为：%s" % alist)
