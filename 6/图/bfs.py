# coding=utf-8
"""
宽度优先遍历
"""


def bfs(node):
    if not node:
        return
    queue = list()
    appear_set = set()
    queue.append(node)
    appear_set.add(node)
    while queue:
        current_node = queue.pop(0)
        print current_node.value
        for next_node in current_node.nexts:
            if next_node not in appear_set:
                queue.append(next_node)
                appear_set.add(next_node)
