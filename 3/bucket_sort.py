# coding=utf-8
def bucket_sort(array):
    """
    最简单的桶排序
    @param array:
    @type array:
    @return:
    @rtype:
    """
    # type: (list) -> array
    max_value = max(array)
    min_value = min(array)
    bucket_list = [[] for _ in range(max_value - min_value + 1)]
    for _value in array:
        bucket_list[_value - min_value].append(_value)
    result = []
    for _bucket in bucket_list:
        if _bucket:
            for _value in _bucket:
                result.append(_value)
    return result


if __name__ == '__main__':
    print bucket_sort([1, 2, 3, 4, 55, 0, 1])
