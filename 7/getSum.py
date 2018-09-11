def get_sum_recursive(array, aim):
    if array:
        return process(array, 0, 0, aim)


def get_sum_dp(array, aim):


def process(array, i, sum, aim):
    # basecase
    if i == len(array):
        return sum == aim

    return process(array, i + 1, sum + array[i], aim) or process(array, i + 1, sum, aim)


if __name__ == '__main__':
    a = [1, 2, 3]
    print get_sum_recursive(a, 7)
