# coding=utf-8
"""
深度优先遍历
"""


def dfs(node):
    if not node:
        return
    stack = list()
    appear_set = set()
    stack.append(node)
    appear_set.add(node)
    print node.value
    while stack:
        current_node = stack.pop()
        for next_node in current_node.nexts:
            if next_node not in appear_set:
                stack.append(current_node)
                stack.append(next_node)
                appear_set.add(next_node)
                print next_node.value
                break
