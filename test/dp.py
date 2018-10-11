def recursive(string1, string2):
    if string1 and string2:
        return process(string1, string2, 0, 0)


def process(string1, string2, index1, index2):
    # basecase
    if index1 == len(string1) or index2 == len(string2):
        return 0

    if string1[index1] == string2[index2]:
        return process(string1, string2, index1 + 1, index2 + 1) + 1
    if string1[index1] != string2[index2]:
        return max(process(string1, string2, index1, index2 + 1), process(string1, string2, index1 + 1, index2))


def dp(string1, string2):
    length1 = len(string1)
    length2 = len(string2)
    dp_array = [[0 for _ in range(length1 + 1)] for _ in range(length2 + 1)]
    for j in reversed(range(length2)):
        for i in reversed(range(length1)):
            if string1[i] == string2[j]:
                dp_array[j][i] = dp_array[j + 1][i + 1] + 1
            else:
                dp_array[j][i] = max(dp_array[j + 1][i], dp_array[j][i + 1])
    return dp_array[0][0]


if __name__ == '__main__':
    print recursive('ABCDE', 'ZBDCDE')
    print dp('ABCDE', 'ZBDCDE')