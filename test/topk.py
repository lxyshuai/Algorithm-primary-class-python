# coding=utf-8
import Queue


###########
# 选择排序 #
############
def topk_selection_sort(array, k):
    """
    选择排序
    @param array:
    @type array:
    @param k:
    @type k:
    @return:
    @rtype:
    """
    if k < 1 or k > len(array):
        return array
    for i in range(1, k + 1):
        max_index = 0
        for j in range(1, len(array) - i + 1):
            if array[j] > array[max_index]:
                max_index = j
        array[-i], array[max_index] = array[max_index], array[-i]
    return array[-10:]


#########
# 堆排序 #
##########
def heapify_non_recursive(array, index, size):
    """
    最大堆
    """
    while index < size:
        largest = index
        left = index * 2 + 1
        right = left + 1
        if left < size and array[left] > array[largest]:
            largest = left
        if right < size and array[right] > array[largest]:
            largest = right
        if largest != index:
            array[largest], array[index] = array[index], array[largest]
            index = largest
        else:
            break


def heapify_recursive(array, index, size):
    left = index * 2 + 1
    right = left + 1
    largest = index
    if left < size and array[index] < array[left]:
        largest = left
    if right < size and array[largest] < array[right]:
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify_recursive(array, largest, size)


def build_max_heap(array):
    size = len(array)
    begin = ((size - 1) - 1) / 2
    for index in range(begin, -1, -1):
        heapify_non_recursive(array, index, size)


def topk_heap_sort(array, k):
    if k < 1 or k > len(array):
        return array
    # 建最大堆
    size = len(array)
    build_max_heap(array)
    for i in range(1, k + 1):
        array[0], array[-i] = array[-i], array[0]
        size -= 1
        heapify_non_recursive(array, 0, size)
    return array[-10:]


########
# 快排 #
########

def select(array, begin, end, i):
    if begin == end:
        return array[begin]


def get_min_kth_by_BFPRT(array, k):
    array_copy = array[:]
    return select(array_copy, 0, len(array_copy) - 1, k - 1)


def topk_quick_sort_BFPRT(array, k):
    if k < 1 or k > len(array):
        return array
    min_kth = get_min_kth_by_BFPRT(array, k)



def get_median(array, begin, end):
    insertion_sort(array, begin, end)
    sum = end + begin
    middle = (sum / 2) + (sum % 2)
    return array[middle]


def insertion_sort(array, begin, end):
    for i in range(begin + 1, end + 1):
        for j in range(i, begin, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break


if __name__ == '__main__':
    array = range(100)
    print topk_selection_sort(array, 10)
    print topk_heap_sort(array, 10)
