# coding=utf-8

def insertion_sort(array):
    """
    插入排序
    时间复杂度:O(N^2)
    额外空间复杂度:O(1)
    Args:
        array:

    Returns:

    """
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

if __name__ == '__main__':
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    insertion_sort(alist)
    print("新列表为：%s" % alist)
