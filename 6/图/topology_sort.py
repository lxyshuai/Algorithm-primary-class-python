# coding=utf-8
"""
拓扑排序算法
适用范围：要求有向图，且有入度为0的节点，且没有环
"""


def topology_sort(graph):
    in_map = dict()
    zero_in_degree_queue = list()
    result_list = list()
    for node in graph.nodes.values():
        in_map[node] = node.in_degree
        if node.in_degree == 0:
            zero_in_degree_queue.append(node)
    while zero_in_degree_queue:
        current_node = zero_in_degree_queue.pop(0)
        result_list.append(current_node)
        for next_node in current_node.nexts:
            in_map[next_node] = in_map.get(next_node) - 1
            if in_map[next_node] == 0:
                zero_in_degree_queue.append(next_node)
    return result_list
