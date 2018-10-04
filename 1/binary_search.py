# coding=utf-8
"""
二分查找递归,非递归实现
二分查找变种:一个有重复元素的数组中查找 key 的最左，右位置
"""


def binary_sort_recursive(array, left, right, number):
    if not array:
        return -1
    middle = left + (right - left) / 2
    if array[middle] < number:
        binary_sort_recursive(array, middle + 1, right, number)
    elif array[middle] > number:
        binary_sort_recursive(array, left, middle - 1, number)
    else:
        return middle
    return -1


def binary_sort_un_recursive(array, number):
    if not array:
        return -1
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = left + (right - left) / 2
        if array[middle] < number:
            left = middle + 1
        elif array[middle] > number:
            right = middle - 1
        else:
            return middle
    return -1


"""
判断第一次出现和最后一次出现 区别 
first 运用了 除法总是向左(下)取整的特点  所以 hi 总是能通过mid 的除法向左和lo汇合 
例如  1  1  中找 1 
mid 总是指向第一个 1  
但 last 就不能用此方法, 还是因为因为除法总是向左边取整的 
3 3  
lo 指向 第一个3 hi 指向第二个 3 
当 mid <= key 
lo = mid 
mid 总是在lo这一边, 此时 lo < hi  永远成立,会造成死循环 
所以遇到这种情况就应该结束循环,将条件改为   lo <  hi - 1 
由于标准中 在lo == hi 循环体内还要判断一次 
frist的解法 也在循环外面 lo == hi时判断了一次 
所以在向右边找最大的时候 
应该先判断 hi  然后 判断lo  
3 3 找 3 的情况  lo 指向第一个3  hi 指向最后一个3 
此时应该返回 hi 而不是lo 
 
 
 3  4  4 5 key = 3 
 结束循环时 (while lo < hi  - 1) 
   hi = 4 lo = 3  
通过判断 应该返回  lo 

"""
def binary_sort_un_recursive_first_appear(array, number):
    """
    二分查找可以有很多变种，变种实现要注意边界值的判断。例如在一个有重复元素的数组中查找 key 的最左位置的实现
    @param array:
    @type array:
    @param number:
    @type number:
    @return:
    @rtype:
    """
    if not array:
        return -1
    left = 0
    right = len(array) - 1
    while left < right:
        middle = left + (right - left) / 2
        if array[middle] >= number:
            right = middle
        else:
            left = middle + 1


def binary_sort_un_recursive_last_appear(array, number):
    """
    二分查找可以有很多变种，变种实现要注意边界值的判断。例如在一个有重复元素的数组中查找 key 的最右位置的实现
    @param array:
    @type array:
    @param number:
    @type number:
    @return:
    @rtype:
    """
    if not array:
        return -1
    left = 0
    right = len(array) - 1
    while left < right - 1:
        middle = left + (right - left) / 2
        if array[middle] <= number:
            left = middle
        else:
            right = middle - 1
    if array[right] == number:
        return right
    elif array[left] == number:
        return left
    else:
        return -1



if __name__ == '__main__':
    print binary_sort_un_recursive_last_appear([1, 2, 2, 2, 2, 2, 2], 2)
