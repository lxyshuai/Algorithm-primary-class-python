# coding=utf-8
"""
给定一个字符串str1，只能往str1的后面添加字符变成str2。
要求1：str2必须包含两个str1，两个str1可以有重合，但是不
能以同一个位置开头。
要求2：str2尽量短
最终返回str2
举例：
str1 = 123，str2 = 123123 时，包含两个str1，且不以相同
位置开头，且str2最短。
str1 = 123123，str2 = 123123123 时，包含两个str1，且不
以相同位置开头，且str2最短。
str1 = 111，str2 = 1111 时，包含两个str1，且不以相同位
置开头，且str2最短。
"""


def answer(string):
    if not string:
        return ""
    if len(string) == 1:
        return string + string
    if len(string) == 2:
        return string + string[0] if string[0] == string[1] else string + string
    match_length = end_next_length(string)
    return string + string[match_length:]


def end_next_length(string):
    char_array = list(string)
    next_array = list()
    next_array.append(-1)
    next_array.append(0)
    position = 2
    while position < len(char_array) + 1:
        current_index = position - 1
        compare_index = next_array[current_index]
        match_length = next_array[current_index]
        while compare_index != -1:
            if char_array[current_index] == char_array[compare_index]:
                next_array.append(match_length + 1)
                position += 1
                break
            else:
                compare_index = next_array[compare_index]
                match_length = next_array[compare_index]
        else:
            next_array.append(0)
            position += 1
    return next_array[len(char_array)]


if __name__ == '__main__':
    print answer("111")
