# coding=utf8
"""
打印两个有序链表的公共部分
【题目】
给定两个有序链表的头指针head1和head2，打印两个链表的公共部分。
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def print_common_part(head1, head2):
    print("Common Part:")
    while head1 and head2:
        if head1.value < head2.value:
            head1 = head1.next
        elif head1.value > head2.value:
            head2 = head2.next
        else:
            print head1.value
            head1 = head1.next
            head2 = head2.next


if __name__ == '__main__':
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)
    node2 = Node(2)
    node2.next = Node(3)
    node2.next.next = Node(4)
    print_common_part(node1, node2)
