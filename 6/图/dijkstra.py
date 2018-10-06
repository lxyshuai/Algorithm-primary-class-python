# coding=utf-8
"""
Dijkstra算法
适用范围：没有权值为负数的边,有向图,没有环(也可有环,要添加判断)
"""
import sys


def get_min_distance_node(distance_map):
    min_node = None
    min_distance = sys.maxint
    for entry in distance_map.items():
        node = entry[0]
        distance = entry[1]
        if distance < min_distance:
            min_node = node
            min_distance = distance
    return min_node


def dijkstra1(head):
    # 记录从head出发到某一个节点的距离
    distance_map = dict()
    distance_map[head] = 0
    # 算过的点,不重复计算
    result_nodes = dict()
    min_node = get_min_distance_node(distance_map)
    while min_node:
        min_distance = distance_map.get(min_node)
        # 因为既要拿相邻点也要拿权值,所以通过边拿
        for edge in min_node.edges:
            to_node = edge.to_node
            if to_node not in distance_map:
                distance_map[to_node] = min_distance + edge.weight
            distance_map[to_node] = min(distance_map.get(to_node), min_distance + edge.weight)
        result_nodes[min_node] = min_distance
        # 避免环的情况,添加判断
        # if len(result_nodes) == :
        #     return result_nodes
        min_node = get_min_distance_node(distance_map)

    return result_nodes
