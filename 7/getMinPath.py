# coding=utf-8
"""
给你一个二维数组，二维数组中的每个数都是正数，要求从左上
角走到右下角，每一步只能向右或者向下。沿途经过的数字要累
加起来。返回最小的路径和
"""
def get_min_path_recursive(matrix):
    if matrix:
        return process_with_cache(matrix, 0, 0)
    return


def get_min_path_dp(matrix):
    if matrix:
        i, j = len(matrix), len(matrix[0])
        dp =[[0 for _ in range(i)]for _ in range(j)]
        # 最右下角
        dp[i - 1][j - 1] = matrix[i - 1][j - 1]
        # 最后一列
        for _i in reversed(range(i - 1)):
            dp[_i][j - 1] = dp[_i + 1][j - 1] + matrix[_i][j - 1]
        # 最后一行
        for _j in reversed(range(j - 1)):
            dp[i - 1][_j] = dp[i - 1][_j + 1] + matrix[i - 1][_j]
        for _i in reversed(range(i - 1)):
            for _j in reversed(range((j - 1))):
                dp[_i][_j] = min(dp[_i][_j + 1], dp[_i + 1][_j]) + matrix[_i][_j]
        return dp[0][0]
    else:
        return



def process(matrix, i, j):
    # 走到了右下角终点
    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        return matrix[i][j]

    # 走到最下边,只能往右走
    if i == len(matrix) - 1:
        return process(matrix, i, j + 1) + matrix[i][j]

    # 走到最右边,只能往下走
    if j == len(matrix[0]) - 1:
        return process(matrix, i + 1, j) + matrix[i][j]

    # 其他,既可以往下走也可以往右走
    else:
        return matrix[i][j] + min(process(matrix, i + 1, j),
                                  process(matrix, i, j + 1))


# 递归做傻缓存
cache = {}


def process_with_cache(matrix, i, j):
    # 走到了右下角终点
    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        result = matrix[i][j]

    # 走到最下边,只能往右走
    elif i == len(matrix) - 1:
        next_key = str(i) + '_' + str(j + 1)
        if cache.has_key(next_key):
            next_value = cache[next_key]
        else:
            next_value = process_with_cache(matrix, i, j + 1)
        result = next_value + matrix[i][j]

    # 走到最右边,只能往下走
    elif j == len(matrix[0]) - 1:
        next_key = str(i + 1) + '_' + str(j)
        if cache.has_key(next_key):
            next_value = cache[next_key]
        else:
            next_value = process_with_cache(matrix, i + 1, j)
        result = next_value + matrix[i][j]

    # 其他,既可以往下走也可以往右走
    else:
        right_next_key = str(i) + '_' + str(j + 1)
        if cache.has_key(right_next_key):
            right_next_value = cache[right_next_key]
        else:
            right_next_value = process_with_cache(matrix, i, j + 1)

        down_next_key = str(i + 1) + '_' + str(j)
        if cache.has_key(down_next_key):
            down_next_value = cache[down_next_key]
        else:
            down_next_value = process_with_cache(matrix, i + 1, j)
        result = matrix[i][j] + min(right_next_value,
                                    down_next_value)
    cache[str(i) + '_' + str(j)] = result
    return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print get_min_path_dp(matrix)
