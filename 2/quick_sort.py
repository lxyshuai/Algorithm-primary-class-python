# coding=utf-8

def quick_sort_inplace_extrance(array):
    if array:
        quick_sort_inplace(array, 0, len(array) - 1)
    else:
        return


def quick_sort_inplace(array, left, right):
    if left < right:
        less, greater = partition(array, left, right)
        quick_sort_inplace(array, left, less)
        quick_sort_inplace(array, greater + 1, right)


v


def partition(array, left, right):
    """
    left开始指向最左边,从左往右遍历.
    right开始指向最右边.right不移动,以right为轴分大小
    less指向最左边-1(left-1)
    greater指向最右边(right)

    遍历过程:
    array[left] > array[right],greater-=1,array[greater]和array[left]交换.因为array[greater]交换前未遍历过(未划分大小),left不移动.
    array[left] < array[right],less+=1,array[less]和array[left]交换.因为less必然比left小,所以array[less]交换前遍历过(划过大小),left+1.
    array[left] == array[right],less+=1
    结束遍历的条件:left遍历完所有的数(即left等于greater,因为greater后面的数必然已经遍历过)


    @param array:
    @type array:
    @param left:
    @type left:
    @param right:
    @type right:
    @return:
    @rtype:
    """
    less = left - 1
    greater = right
    while left != greater:
        if array[left] > array[right]:
            greater -= 1
            array[greater], array[left] = array[left], array[greater]
        elif array[left] < array[right]:
            less += 1
            array[less], array[left] = array[left], array[less]
            left += 1
        elif array[left] == array[right]:
            left += 1
    return


def quick_sort_simple(array):
    """
    暴力的快排
    @param array:
    @type array:
    @return:
    @rtype:
    """
    if len(array) > 1:
        less = []
        greater = []
        base = array.pop()

        for _number in array:
            if _number < base:
                less.append(_number)
            else:
                greater.append(_number)
        return quick_sort_simple(less) + [base] + quick_sort_simple(greater)
    else:
        return array


if __name__ == '__main__':
    array = [3, 2, 4, 5, 1]
    print quick_sort_simple(array)
    print array
