# coding=utf-8
"""
反转单向和双向链表
【题目】
分别实现反转单向链表和反转双向链表的函数。
【要求】
如果链表长度为N，时间复杂度要求为O(N)，额外空间复杂度要求为O(1)
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


def reverse_list(head):
    pointed_to_node = head
    changed_node = head.next
    head.next = None
    while changed_node:
        next_to_be_changed_node = changed_node.next
        changed_node.next = pointed_to_node
        pointed_to_node = changed_node
        changed_node = next_to_be_changed_node
    return pointed_to_node


class DoubleNode(object):
    def __init__(self, value):
        self.value = value
        self.last = None
        self.next = None

    def __str__(self):
        return str(self.value)


def reverse_double_list(head):
    pre = None
    next = None
    while head:
        next = head.next
        head.next = pre
        head.last = next
        pre = head
        head = next

    return  pre

if __name__ == '__main__':
    # 1->2->3->4->5->6->7->null
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    result = reverse_list(head1)
    print result


    head2 = DoubleNode(1)
    head2.next = DoubleNode(2)
    head2.next.last = head2
    head2.next.next = DoubleNode(3)
    head2.next.next.last = head2.next
    head2.next.next.next = DoubleNode(4)
    head2.next.next.next.last = head2.next.next
    result = reverse_double_list(head2)
    print result
