# coding=utf-8
"""
给定两个二叉树T1和T2，返回T1的某个子树结构是否与T2的结构相等。
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


##################
# 序列化后kmp解法 #
##################
def serial_tree_by_pre_traversal(root):
    if not root:
        return "!#!"
    result = "!" + str(root.value) + "!"
    result += str(serial_tree_by_pre_traversal(root.left))
    result += str(serial_tree_by_pre_traversal(root.right))
    return result


def is_sub_tree_kmp(tree1, tree2):
    serial1 = serial_tree_by_pre_traversal(tree1)
    serial2 = serial_tree_by_pre_traversal(tree2)
    return get_index_of(serial1, serial2) != -1


def get_index_of(word, match):
    if not word:
        return -1
    if not match:
        return -1
    if len(match) > len(word):
        return -1
    match_index = 0
    word_index = 0
    next_array = get_next_array(match)
    while match_index < len(match) and word_index < len(word):
        if word[word_index] == match[match_index]:
            word_index += 1
            match_index += 1
        elif next_array[match_index] == -1:
            word_index += 1
        else:
            match_index = next_array[match_index]

    return word_index - match_index if match_index == len(match) else -1


def get_next_array(match):
    if len(match) == 1:
        return [-1]
    next_array = list()
    next_array.append(-1)
    next_array.append(0)
    position = 2
    while position < len(match):
        current_index = position - 1
        compare_index = next_array[current_index]
        match_length = compare_index
        while compare_index != -1:
            if match[current_index] == match[compare_index]:
                next_array.append(match_length + 1)
                position += 1
                break
            else:
                compare_index = next_array[compare_index]
                match_length = compare_index
        else:
            next_array.append(0)
            position += 1
    return next_array


#################
# 二叉树遍历解法 #
#################
def is_same_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if tree1.value == tree2.value:
        return is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)


def is_sub_tree(tree, subtree):
    if not tree:
        return False
    if is_same_tree(tree, subtree):
        return True
    return is_sub_tree(tree.left, subtree) or is_sub_tree(tree.right, subtree)


if __name__ == '__main__':
    t1 = Node(1)
    t1.left = Node(2)
    t1.right = Node(3)
    t1.left.left = Node(4)
    t1.left.right = Node(5)
    t1.right.left = Node(6)
    t1.right.right = Node(7)
    t1.left.left.right = Node(8)
    t1.left.right.left = Node(9)

    t2 = Node(2)
    t2.left = Node(4)
    t2.left.right = Node(8)
    t2.right = Node(5)
    t2.right.left = Node(9)

    import datetime
    start = datetime.datetime.now()
    for _ in range(10000):
        is_sub_tree_kmp(t1, t2)
    end = datetime.datetime.now()
    print end - start
    start = datetime.datetime.now()
    for _ in range(10000):
        is_sub_tree(t1, t2)
    end = datetime.datetime.now()
    print end - start

