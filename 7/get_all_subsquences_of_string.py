# coding=utf-8
"""
打印一个字符串的所有子序列
"""

def get_all_sub_of_string(string):
    process(string,0,'')
    print ''

def process(origin_string, index, pre_string):
    if index == len(origin_string):
        if pre_string != '':
            print pre_string
        return

    process(origin_string, index + 1, pre_string + origin_string[index])
    process(origin_string, index + 1, pre_string)


if __name__ == '__main__':
    get_all_sub_of_string('abc')