# coding=utf8
"""
给定两个数组w和v，两个数组长度相等，w[i]表示第i件商品的
重量，v[i]表示第i件商品的价值。
再给定一个整数bag，要求你挑选商品的重量加起来一定不能超
过bag，返回满足这个条件下，你能获得的最大价值。
"""
import sys


def get_max_value_recursive(weight_list, value_list, bag):
    if weight_list and value_list:
        return process(weight_list, value_list, 0, 0, bag)


def get_max_value_dp(weight_list, value_list, bag):
    i = len(weight_list)
    j = max(weight_list) + bag
    dp = [[0 for _ in range(j + 1)] for _ in range(i + 1)]

    for _i in range(i + 1):
        for _j in range(bag + 1, j + 1):
            dp[_i][_j] = -sys.maxint

    for _j in range(0, bag + 1):
        dp[i][_j] = 0

    for _i in reversed(range(0, i)):
        for _j in range(0, bag + 1):
            dp[_i][_j] = max(dp[_i + 1][_j + weight_list[_i]] + value_list[_i], dp[_i + 1][_j])
    return dp[0][0]


def get_max_value_dp2(weight_list, value_list, bag):
    i = len(weight_list)
    j = bag
    dp = [[0 for _ in range(j + 1)] for _ in range(i + 1)]

    for _j in range(0, j + 1):
        dp[i][_j] = 0

    for _i in reversed(range(0, i)):
        for _j in range(0, j + 1):
            if _j + weight_list[_i] <= bag:
                dp[_i][_j] = max(dp[_i + 1][_j + weight_list[_i]] + value_list[_i], dp[_i + 1][_j])
            else:
                dp[_i][_j] = dp[_i + 1][_j]
    return dp[0][0]


def process(weight_list, value_list, i, sum, bag):
    # basecase 到了最后一个数后面的一个数(不存在)
    if i == len(weight_list):
        if sum > bag:
            return -sys.maxint
        return 0
    return max(process(weight_list, value_list, i + 1, sum, bag),
               process(weight_list, value_list, i + 1, sum + weight_list[i], bag) + value_list[i])


if __name__ == '__main__':
    weight_list = [3, 2, 4, 7]
    value_list = [5, 6, 3, 19]
    bag = 10
    print get_max_value_recursive(weight_list, value_list, 11)
    print get_max_value_dp(weight_list, value_list, 11)
    print get_max_value_dp2(weight_list, value_list, 11)
