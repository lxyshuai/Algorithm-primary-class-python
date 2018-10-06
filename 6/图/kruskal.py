# coding=utf-8
"""
最小生成树算法:在保证图连通的情况下,需要的边的权重的集合最小
kruskal算法
适用范围：要求无向图
通过考察边,一条边的引入会让边两头的集合合成一个集合,牵扯到两个集合合并问题,用并查集
"""
import Queue


class UnionFindSet(object):
    def __init__(self):
        # (key,value)表示key的父节点是value.例如:(DATA_A,DATA_B)代表DATA_A的父节点是DATA_B
        self.father_map = dict()
        # (key,value)表示key所在的集合的size是value
        self.size_map = dict()

    def make_sets(self, node_list):
        """
        要使用并查集,需要一开始将所有元素给出
        @param node_list:
        @type node_list:
        @return:
        @rtype:
        """
        self.father_map.clear()
        self.size_map.clear()
        for node in node_list:
            self.father_map[node] = node
            self.size_map[node] = 1

    def find_representation_recursive(self, node):
        """
        找到代表结点,并将沿途的节点全部打平指向代表节点,递归版本
        @return:
        @rtype:
        """
        father_node = self.father_map.get(node)
        if father_node != node:
            father_node = self.find_representation_recursive(father_node)
        self.father_map[node] = father_node
        return father_node

    def find_representation_un_recursive(self, node):
        """
        找到代表结点,并将沿途的节点全部打平指向代表节点,并非递归版本
        @return:
        @rtype:
        """
        changed_node = []
        father_node = self.father_map.get(node)
        while node != father_node:
            changed_node.append(father_node)
            node = father_node
            father_node = self.father_map.get(node)
        for _node in changed_node:
            self.father_map[_node] = father_node
        return father_node

    def is_same_set(self, node1, node2):
        return self.find_representation_recursive(node1) == self.find_representation_un_recursive(node2)

    def union(self, node1, node2):
        if node1 == None or node2 == None:
            return
        head1 = self.find_representation_recursive(node1)
        head2 = self.find_representation_recursive(node2)
        if head1 != head2:
            size1 = self.size_map.get(head1)
            size2 = self.size_map.get(head2)
            if size1 > size2:
                self.father_map[head2] = head1
                self.size_map[head1] = size1 + size2
            else:
                self.father_map[head1] = head2
                self.size_map[head2] = size1 + size2


def kruskal_MST(graph):
    union_find_set = UnionFindSet()
    union_find_set.make_sets(graph.nodes.values())
    edge_priority_queue = Queue.PriorityQueue()
    # 将图中全部边加入优先级队列
    for _edge in graph.edges:
        edge_priority_queue.put(_edge)
    edge_result_set = set()
    while edge_priority_queue.qsize() != 0:
        current_edge = edge_priority_queue.get()
        from_node = current_edge.from_node
        to_node = current_edge.to_node
        if not union_find_set.is_same_set(from_node, to_node):
            edge_result_set.add(current_edge)
            union_find_set.union(from_node, to_node)
    return edge_result_set
