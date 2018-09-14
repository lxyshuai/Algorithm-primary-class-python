# coding=utf-8
"""
打印一个字符串的所有子排序
"""


def get_all_permutations_of_string(string):
    string_list = list(string)
    process(string_list, 0)


def process(string_list, index):
    # basecase
    if index == len(string_list):
        print ''.join(string_list)
    for _i in range(index, len(string_list)):
        string_list[index], string_list[_i] = string_list[_i], string_list[index]
        process(string_list, index + 1)
        # string_list[_i], string_list[index] = string_list[index], string_list[_i]


if __name__ == '__main__':
    get_all_permutations_of_string('abcd')
