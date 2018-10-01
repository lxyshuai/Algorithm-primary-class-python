# coding=utf8
"""
将单向链表按某值划分成左边小、中间相等、右边大的形式
【题目】
给定一个单向链表的头节点head，节点的值类型是整型，再给定一个整
数pivot。实现一个调整链表的函数，将链表调整为左部分都是值小于
pivot的节点，中间部分都是值等于pivot的节点，右部分都是值大于
pivot的节点。除这个要求外，对调整后的节点顺序没有更多的要求。
例如：链表9->0->4->5->1，pivot=3。
调整后链表可以是1->0->4->9->5，也可以是0->1->9->5->4。总之，满
足左部分都是小于3的节点，中间部分都是等于3的节点（本例中这个部
分为空），右部分都是大于3的节点即可。对某部分内部的节点顺序不做
要求。
如果链表长度为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1)。
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def list_partition(head, pivot):
    if head == None:
        return
    if head.next == None:
        return head

    # 第一次遍历找到链表的最大最小值等于值的三个节点
    smaller_head = None
    smaller_tail = None
    equal_head = None
    equal_tail = None
    bigger_head = None
    bigger_tail = None
    next = None
    while head:
        next = head.next
        head.next = None

        if head.value > pivot:
            if bigger_head:
                bigger_tail.next = head
            else:
                bigger_head = head
            bigger_tail = head
        elif head.value < pivot:
            if smaller_head:
                smaller_tail.next = head
            else:
                smaller_head = head
            smaller_tail = head
        else:
            if equal_head:
                equal_tail.next = head
            else:
                equal_head = head
            equal_tail = head
        head = next

    # 将smaller和equal合并
    if smaller_tail:
        smaller_tail.next = equal_head
        equal_tail = smaller_tail if equal_tail == None else equal_tail

    # 将三部分合并
    if equal_tail:
        equal_tail.next = bigger_head

    # 找出开始的头结点
    if smaller_head:
        return smaller_head
    elif equal_head:
        return equal_head
    else:
        return bigger_head


if __name__ == '__main__':
    head = Node(19)
    head.next = Node(19)
    head.next.next = Node(31)
    head.next.next.next = Node(20)
    head.next.next.next.next = Node(19)
    result = list_partition(head, 32)
    print result
