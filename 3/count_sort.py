# coding=utf-8
def count_sort(array):
    """
    计数排序
    @param array:
    @type array:
    @return:
    @rtype:
    """
    if not array:
        return
    max_value = max(array)
    bucket = [0 for _ in range(max_value + 1)]
    for _value in array:
        bucket[_value] += 1
    result = []
    for _index, _value in enumerate(bucket):
        result.extend([_index for _ in range(_value)])
    return result

if __name__ == '__main__':
    print count_sort([1,2,4,1,2])
