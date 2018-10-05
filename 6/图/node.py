# coding=utf-8
class Node(object):
    def __init__(self,value):
        self.value = value
        # 入度,有多少个节点指向我
        self.in_degree = 0
        # 出度,我指向多少个节点
        self.out_degree = 0
        # 从我出发能到达的下一个节点,邻居节点
        self.nexts = list()
        # 从我出发发散出去边的集合
        self.edges = list()