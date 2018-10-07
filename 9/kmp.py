# coding=utf-8
"""
kmp
"""


def get_next_array(match):
    char_array = list(match)
    next_array = list()
    next_array.append(-1)
    next_array.append(0)
    position = 2
    while position < len(char_array):
        compare_index = next_array[position - 1]
        next_number = next_array[position - 1]
        while compare_index != -1:
            if match[position - 1] == match[compare_index]:
                next_array.append(next_number + 1)
                position += 1
                break
            else:
                compare_index = next_array[compare_index]
                next_number = next_array[compare_index]
        else:
            next_array.append(0)
            position += 1
    return next_array


def get_index(word, match):
    if not word:
        return -1
    if not match:
        return -1
    if len(word) < len(match):
        return -1
    word_char_array = list(word)
    match_char_array = list(match)
    word_index = 0
    match_index = 0
    next_array = get_next_array(match)
    while word_index < len(word_char_array) and match_index < len(match_char_array):
        if word_char_array[word_index] == match_char_array[match_index]:
            word_index += 1
            match_index += 1
        elif match_index == -1:
            word_index += 1
        else:
            match_index = next_array[match_index]

    return word_index - match_index if match_index == len(match_char_array) else -1


if __name__ == '__main__':
    print get_next_array("abcdabd")
    print get_index("abcabcababaccc", "ababa")
