def getMin(array, left, right):
    if left == right:
        return array[left]

    middle = left + (right - left) / 2
    leftMin = getMin(array, left, middle)
    rightMin = getMin(array, middle + 1, right)
    return min(leftMin, rightMin)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    print getMin(array, 0, len(array) - 1)
