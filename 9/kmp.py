# coding=utf-8
"""
kmp
"""
def get_next_array(word):
    char_array = list(word)
    if len(char_array) == 1:
        return [-1]
    next = list()
    next.append(-1)
    next.append(0)
    position = 2
    # 用于比对的index
    current_index = 0
    while position < len(char_array):
        if char_array[position - 1] == char_array[current_index]:
            current_index += 1
            next.append(current_index)
            position += 1
        elif current_index > 0:
            current_index = next[current_index]
        else:
            next.append(0)
            position += 1
    return next


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
        elif next_array[match_index] == -1:
            word_index += 1
        else:
            match_index = next_array[match_index]

    return word_index - match_index if match_index == len(match_char_array) else -1


if __name__ == '__main__':
    print get_index("abcabcababaccc","ababa")
