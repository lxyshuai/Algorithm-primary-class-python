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

def topk_quick_sort_BFPRT(array, k):
    if k < 1 or k > len(array):
        return array
    min_kth = get_min_kth_by_BFPRT(array, k)
    result = []
    for number in array:
        if number < min_kth:
            result.append(array[number])
    result.append(min_kth)
    return result


def get_min_kth_by_BFPRT(array, k):
    array_copy = array[:]
    return select(array_copy, 0, len(array_copy) - 1, k - 1)


def select(array, begin, end, k):
    if begin == end:
        return array[begin]
    pivot = median_of_Medians(array, begin, end)
    equal_range = partition_range(array, begin, end, pivot)
    if equal_range[0] <= k <= equal_range[1]:
        return array[k]
    elif k < equal_range[0]:
        return select(array, begin, equal_range[0] - 1, k)
    else:
        return select(array, equal_range[1] + 1, end, k)


def partition_range(array, begin, end, pivot_value):
    """
    返回等于去的数组范围
    @param array:
    @type array:
    @param begin:
    @type begin:
    @param end:
    @type end:
    @param pivot_value:
    @type pivot_value:
    @return:
    @rtype:
    """
    small_index = begin - 1
    big_index = end + 1
    current_index = begin
    while current_index != big_index:
        if array[current_index] < pivot_value:
            small_index += 1
            array[small_index], array[current_index] = array[current_index], array[small_index]
            current_index += 1
        elif array[current_index] > pivot_value:
            big_index -= 1
            array[big_index], array[current_index] = array[current_index], array[big_index]
        else:
            current_index += 1
    return small_index + 1, big_index - 1


def median_of_Medians(array, begin, end):
    number = end - begin + 1
    offset = 0 if number % 5 == 0 else 1
    median_array = []
    for index in range(0, number / 5 + offset):
        begin_index = begin + index * 5
        end_index = begin_index + 4
        median_array.append(get_median(array, begin_index, min(end_index, end)))
    return select(median_array, 0, len(median_array) - 1, len(median_array) / 2)


def get_median(array, begin, end):
    """
    获得数组指定范围的中位数
    @param array:
    @type array:
    @param begin:
    @type begin:
    @param end:
    @type end:
    @return:
    @rtype:
    """
    insertion_sort(array, begin, end)
    sum = end + begin
    middle = (sum / 2) + (sum % 2)
    return array[middle]


def insertion_sort(array, begin, end):
    """
    在数组特定范围进行局部插入排序
    @param array:
    @type array:
    @param begin:
    @type begin:
    @param end:
    @type end:
    @return:
    @rtype:
    """
    for i in range(begin + 1, end + 1):
        for j in range(i, begin, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break


if __name__ == '__main__':
    array = range(100)
    # print topk_selection_sort(array, 10)
    # print topk_heap_sort(array, 10)
    print topk_quick_sort_BFPRT(array, 10)
