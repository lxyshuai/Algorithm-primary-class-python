# coding=utf-8
def merge(array, left, middle, right):
    """
    左边的数比右边的数小的时候，右边的数到末尾的位移为比左边数大的数的数量
    @param array:
    @param left:
    @param middle:
    @param right:
    @return:
    """
    help = []
    p1 = left
    p2 = middle + 1
    result = 0
    while p1 <= middle and p2 <= right:
        if array[p1] < array[p2]:
            result += array[p1] * (right - p2 + 1)
            help.append(array[p1])
            p1 += 1
        else:
            help.append(array[p2])
            p2 += 1

    if p1 <= middle:
        help.extend(array[p1:middle + 1])
    if p2 <= right:
        help.extend(array[p2:right + 1])

    array[left:right + 1] = help

    return result


def merge_sort(array, left, right):
    if left == right:
        return 0
    middle = left + (right - left) / 2
    return merge_sort(array, left, middle) + merge_sort(array, middle + 1, right) + merge(array, left, middle, right)


def get_small_sum(array):
    return merge_sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    print get_small_sum([4, 1, 3, 5, 0, 6])
