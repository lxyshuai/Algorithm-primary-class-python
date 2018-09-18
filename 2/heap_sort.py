# coding=utf-8
"""
用数组实现完全二叉树
根节点从0开始计算
i节点的左节点为2i+1(设i在第j层，i的左子节点在第j+1层，
                 j层最左的节点为a = 0+2^0+2^1+...+2^j,j+1层最左的节点为b = 0+2^0+2^1+...+2^j+2^(j+1),
                 j的左子节点为b + (i - a) * 2 = b - 2a + 2i = 2i + 1
i节点的右节点为2i+2
i节点的父节点为(i-1)/2
"""


def heap_sort(array):
    if not array:
        return array
    else:
        for index in range(0, len(array)):
            heap_insert(array, index)
        size = len(array)
        array[0], array[-1] = array[-1], array[0]
        size -= 1
        while size > 0:
            heapify(array, size)
            size -= 1
            array[0], array[size] = array[size], array[0]


def heap_insert(array, index):
    while array[index] > array[(index - 1) / 2]:
        if (index - 1) / 2 < 0:
            break
        array[index], array[(index - 1) / 2] = array[(index - 1) / 2], array[index]
        index = (index - 1) / 2


def heapify(array, size):
    index = 0
    left = index * 2 + 1
    while left < size:
        right = left + 1
        # 如果有有右子节点，找出左右子节点中较大者；若无右子节点，则为左子节点
        if right < size:
            if array[left] > array[right]:
                largest = left
            else:
                largest = right
        else:
            largest = left

        # 比较该节点与子节点的大小
        if array[index] < array[largest]:
            array[index], array[largest] = array[largest], array[index]
            index = largest
            left = index * 2 + 1
        else:
            break


if __name__ == '__main__':
    array = [3, 31, 2, 3]
    heap_sort(array)
    print array
