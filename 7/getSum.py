# coding=utf-8
def get_sum_recursive(array, aim):
    if array:
        return process(array, 0, 0, aim)


def get_sum_dp(array, aim):
    i = len(array)
    j = sum(array) + 1
    if aim > j - 1:
        return False
    dp = [[False for _ in range(j)] for _ in range(i)]
    # 最后一行为False
    for _j in range(j):
        dp[i - 1][_j] = False
    # sum==aim and _i = i -1 => True
    dp[i - 1][aim] = True

    for _i in reversed(range(i - 1)):
        for _j in range(j):
            if _j + array[_i] > j - 1:
                dp[_i][_j] = dp[_i + 1][_j]
            else:
                dp[_i][_j] = dp[_i + 1][_j] or dp[_i + 1][_j + array[_i]]
    return dp[0][aim]


def process(array, i, sum, aim):
    # basecase
    if i == len(array):
        return sum == aim

    return process(array, i + 1, sum + array[i], aim) or process(array, i + 1, sum, aim)


if __name__ == '__main__':
    a = [1, 2, 3]
    print get_sum_recursive(a, 7)
    print get_sum_dp(a, 4)
