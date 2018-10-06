# coding=utf-8
"""
最小生成树算法:在保证图连通的情况下,需要的边的权重的集合最小
prim算法
适用范围：要求无向图
通过考察点,总从一个点出发找到一个新的点加入集合,不牵扯到两个集合合并问题,用hashset就可以
"""
from random import choice

import Queue


def prim_MST(graph):
    edge_priority_queue = Queue.PriorityQueue()
    node_set = set()
    edge_result_set = set()
    # 随机选择一个开始节点
    random_node = choice(graph.nodes.values())
    node_set.add(random_node)
    for _edge in random_node.edges:
        edge_priority_queue.put(_edge)

    while edge_priority_queue.qsize() != 0:
        current_edge = edge_priority_queue.get()
        to_node = current_edge.to_node
        if to_node not in node_set:
            node_set.add(to_node)
            edge_result_set.add(current_edge)
            for _edge in to_node.edges:
                edge_priority_queue.put(_edge)
    return result
