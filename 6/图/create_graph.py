# coding=utf-8
"""
1）邻接表
2）邻接矩阵
如何表达图？生成图？
"""
from edge import Edge
from graph import Graph
from node import Node


def create_graph(matrix):
    """

    @param matrix:
    [
        [weight,from,to],
        [weight,from,to],
        [weight,from,to],
    ]
    @type matrix:
    @return:
    @rtype:
    """
    graph = Graph()
    for _weight, _from, _to in matrix:
        if not graph.nodes.has_key(_from):
            graph.nodes[_from] = Node(_from)
        if not graph.nodes.has_key(_to):
            graph.nodes[_to] = Node(_to)
        from_node = graph.nodes.get(_from)
        to_node = graph.nodes.get(_to)
        new_edge = Edge(_weight, from_node, to_node)
        from_node.nexts.append(to_node)
        from_node.out_degree += 1
        to_node.in_degree += 1
        from_node.edges.append(new_edge)
        graph.edges.append(new_edge)
    return graph
