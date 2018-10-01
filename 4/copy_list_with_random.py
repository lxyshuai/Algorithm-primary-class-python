# coding=utf8
"""
复制含有随机指针节点的链表
【题目】
一种特殊的链表节点类描述如下：
public class Node {
    public int value;
    public Node next;
    public Node rand;
    public Node(int data) {
    this.value = data;
    }
}
Node类中的value是节点值，next指针和正常单链表中next指针的意义一
样，都指向下一个节点，rand指针是Node类中新增的指针，这个指针可
能指向链表中的任意一个节点，也可能指向null。
给定一个由Node节点类型组成的无环单链表的头节点head，请实现一个
函数完成这个链表中所有结构的复制，并返回复制的新链表的头节点。
进阶：不使用额外的数据结构，只用有限几个变量，且在时间复杂度为
O(N)内完成原问题要实现的函数。
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.random = None


def copy_list_with_random_using_map(head):
    map = dict()
    current_node = head
    while current_node:
        map[current_node] = Node(current_node.value)
        current_node = current_node.next

    current_node = head
    while current_node:
        map.get(current_node).next = current_node.next
        map.get(current_node).random = current_node.random
        current_node = current_node.next

    return map.get(head)


def copy_list_with_random_using_copy(head):
    # 在每个节点后面复制一个相同节点
    current_node = head
    while current_node:
        current_node_copy = Node(current_node.value)
        current_node_copy.next = current_node.next
        current_node.next = current_node_copy
        current_node = current_node_copy.next

    # 将复制节点的随机节点指向修正
    current_node = head
    while current_node:
        current_node.next.random = current_node.random
        current_node = current_node.next.next

    # 分离复制的链表和原链表
    result = head.next
    current_node = head
    while current_node:
        current_node_next = current_node.next.next
        current_node_copy = current_node.next
        current_node.next = current_node_next
        current_node_copy.next = current_node_next.next if current_node_next != None else None
        current_node = current_node.next

    return result


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node1.random = node3
    node2.random = node1

    result1 = copy_list_with_random_using_map(node1)
    result2 = copy_list_with_random_using_copy(node1)
    print 'success'
