# coding=utf8
"""
找出无序数组排序后,相邻值间最大间距
"""


def get_max_gap(array):
    if not array or len(array) < 2:
        return 0
    max_value = max(array)
    min_value = min(array)
    if max_value == min_value:
        return 0
    length = len(array)

    max_bucket = [0 for _ in range(length + 1)]
    min_bucket = [0 for _ in range(length + 1)]
    has_number = [False for _ in range(length + 1)]

    for _value in array:
        bucket_index = select_bucket(_value, length, max_value, min_value)
        max_bucket[bucket_index] = max(max_bucket[bucket_index], _value) if has_number[bucket_index] else _value
        min_bucket[bucket_index] = min(min_bucket[bucket_index], _value) if has_number[bucket_index] else _value
        has_number[bucket_index] = True

    last_max = max_bucket[0]
    result = 0
    for _index in range(1, length + 1):
        if has_number[_index]:
            result = max(result, min_bucket[_index] - last_max)
            last_max = max_bucket[_index]

    return result


def select_bucket(number, length, max, min):
    return int((number - min) * length / (max - min))


if __name__ == '__main__':
    print get_max_gap([1, 3, 3, 5, 10])
