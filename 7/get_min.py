# coding=utf-8
"""
求数组中最小的数
"""
def get_min(array, left, right):
    if left == right:
        return array[left]

    middle = left + (right - left) / 2
    leftMin = get_min(array, left, middle)
    rightMin = get_min(array, middle + 1, right)
    return min(leftMin, rightMin)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    print get_min(array, 0, len(array) - 1)
