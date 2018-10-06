# coding=utf-8
"""
宽度优先遍历
1，利用队列实现
2，从源节点开始依次按照宽度进队列，然后弹出
3，每弹出一个点，把该节点所有没有进过队列的邻接点放入队列
4，直到队列变空
"""


def bfs(node):
    if not node:
        return
    queue = list()
    appear_set = set()
    queue.append(node)
    appear_set.add(appear_set)
    while queue:
        current_node = queue.pop(0)
        print current_node.value
        for next_node in current_node.next:
            if next_node not in appear_set:
                queue.append(next_node)
                appear_set.add(next_node)
