# coding=utf-8
"""
母牛每年生一只母牛，新出生的母牛成长三年后也能每年生一只
母牛，假设不会死。求N年后，母牛的数量。
"""
def get_cow_number(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    return get_cow_number(n - 1) + get_cow_number(n - 3)