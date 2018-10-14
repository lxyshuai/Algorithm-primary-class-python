# coding=utf-8
def get_index(word, match):
    if not word:
        return -1
    if not match:
        return -1
    if len(match) > len(word):
        return -1
    word_index = 0
    match_index = 0
    next_array = get_next_array(match)
    while word_index < len(word) and match_index < len(match):
        if word[word_index] == match[match_index]:
            word_index += 1
            match_index += 1
        elif next_array[match_index] == -1:
            word_index += 1
        else:
            match_index = next_array[match_index]
    if match_index == len(match):
        return word_index - match_index
    else:
        return -1


def get_next_array(match):
    next_array = list()
    # 0位置规定为-1
    next_array.append(-1)
    # 1位置不用计算也知道为0
    next_array.append(0)
    position = 2
    while position < len(match):
        current_index = position - 1
        match_length = next_array[current_index]
        compare_index = next_array[current_index]
        while compare_index != -1:
            if match[compare_index] == match[current_index]:
                next_array.append(match_length + 1)
                position += 1
                break
            else:
                compare_index = next_array[compare_index]
                match_length = next_array[compare_index]
        else:
            next_array.append(0)
            position += 1
    return next_array


def is_rotation(string1, string2):
    if not string1 or not string2:
        return False
    if len(string1) != len(string2):
        return False
    if get_index(string1 + string1, string2) != -1:
        return True
    else:
        return False


if __name__ == '__main__':
    print is_rotation('abc', 'bca')
