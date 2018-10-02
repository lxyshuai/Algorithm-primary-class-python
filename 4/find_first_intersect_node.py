# coding=utf-8
"""
两个单链表相交的一系列问题
【题目】
在本题中，单链表可能有环，也可能无环。给定两个单链表的头节点
head1和head2，这两个链表可能相交，也可能不相交。请实现一个函数，
如果两个链表相交，请返回相交的第一个节点；如果不相交，返回null
即可。
要求：如果链表1的长度为N，链表2的长度为M，时间复杂度请达到
O(N+M)，额外空间复杂度请达到O(1)。
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


def get_loop_node(head):
    """
    寻找单链表是否有环,有环返回入环节点,无环返回None
    @param head:
    @type head:
    @return:
    @rtype:
    """
    if not head and not head.next and not head.next.next:
        return None
    fast_node = head
    slow_node = head
    fast_node = fast_node.next.next
    slow_node = slow_node.next
    # 寻找快慢节点第一次相遇
    while slow_node != fast_node:
        if fast_node.next == None or slow_node.next.next == None:
            return None
        fast_node = fast_node.next.next
        slow_node = slow_node.next

    # 快节点回到头部
    fast_node = head
    # 再次相遇,则为入环节点
    while slow_node != fast_node:
        slow_node = slow_node.next
        fast_node = fast_node.next

    return fast_node


def no_loop(head1, head2):
    current_node1 = head1
    current_node2 = head2
    length1 = 0
    length2 = 0
    while current_node1:
        length1 += 1
        current_node1 = current_node1.next
    while current_node2:
        length2 += 1
        current_node2 = current_node2.next

    # 如果尾节点不相同必然不相交
    if current_node1 != current_node2:
        return None

    current_node1 = head1
    current_node2 = head2
    if length2 > length1:
        for _ in range(length2 - length1):
            current_node2 = current_node2.next
    elif length2 < length1:
        for _ in range(length1 - length2):
            current_node1 = current_node1.next

    while current_node1 != current_node2:
        current_node1 = current_node1.next
        current_node2 = current_node2.next
    return current_node1


def both_loop(head1, loop1, head2, loop2):
    # 如果入环节点相同
    if loop1 == loop2:
        current_node1 = head1
        current_node2 = head2
        length1 = 0
        length2 = 0
        while current_node1 != loop1:
            length1 += 1
            current_node1 = current_node1.next
        while current_node2 != loop2:
            length2 += 1
            current_node2 = current_node2.next

        current_node1 = head1
        current_node2 = head2
        if length2 > length1:
            for _ in range(length2 - length1):
                current_node2 = current_node2.next
        elif length2 < length1:
            for _ in range(length1 - length2):
                current_node1 = current_node1.next

        while current_node1 != current_node2:
            current_node1 = current_node1.next
            current_node2 = current_node2.next
        return current_node1
    else:
        current_node1 = loop1.next
        while current_node1 != loop1:
            if current_node1 == loop2:
                return loop1
            current_node1 = current_node1.next
    return None


def get_intersect_node(head1, head2):
    if head1 == None or head2 == None:
        return None

    loop1 = get_loop_node(head1)
    loop2 = get_loop_node(head2)
    # 两个链表都没有环
    if loop1 == None and loop2 == None:
        return no_loop(head1, head2)
    # 一个链表有环,一个链表没有环,不可能相交
    elif (loop1 == None and loop2 != None) or (
            loop2 == None and loop1 != None):
        return None
    # 两个链表都有环
    elif loop1 != None and loop2 != None:
        return both_loop(head1, loop1, head2, loop2)


if __name__ == '__main__':
    # 两个链表都无环
    # 1->2->3->4->5->6->7->null
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    # 0->9->8->6->7->null
    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next.next.next.next.next  # 8->6
    result = get_intersect_node(head1, head2)
    print result

    # 两个链表都有环,交点在环外面
    # 1->2->3->4->5->6->7->4...
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    head1.next.next.next.next.next.next = head1.next.next.next  # 7->4
    # 0->9->8->2...
    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next = head1.next  # 8->2
    result = get_intersect_node(head1, head2)
    print result

    # 两个链表都有环,交点在环内
    # 1->2->3->4->5->6->7->4...
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    head1.next.next.next.next.next.next = head1.next.next.next  # 7->4
    # 0->9->8->6->4->5->6..
    head2 = Node(0)
    head2.next = Node(9)
    head2.next.next = Node(8)
    head2.next.next.next =head1.next.next.next.next.next; # 8->6
    result = get_intersect_node(head1, head2)
    print result