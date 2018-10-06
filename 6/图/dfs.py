# coding=utf-8
"""
深度优先遍历
1，利用栈实现
2，从源节点开始把节点按照深度放入栈，然后弹出
3，每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
4，直到栈变空
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
