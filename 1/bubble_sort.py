# coding=utf-8
def bubble_sort(array):
    # type: (list[int]) -> None
    """
    冒泡排序
    时间复杂度:O(N^2)
    额外空间复杂度:O(1)
    第一轮把最大的数冒泡到最后
    第二轮把第二大的数冒泡到最后
    ...
    最后一轮把最小的数放到第一
    @param array:
    @return: 
    """
    if not array:
        return
    for i in reversed(range(0, len(array) - 1)):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == '__main__':
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    bubble_sort(alist)
    print("新列表为：%s" % alist)
