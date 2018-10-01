# coding=utf8
"""
判断一个链表是否为回文结构
【题目】
给定一个链表的头节点head，请判断该链表是否为回文结构。
例如：
1->2->1，返回true。
1->2->2->1，返回true。
15->6->15，返回true。
1->2->3，返回false。
进阶：
如果链表长度为N，时间复杂度达到O(N)，额外空间复杂度达到O(1)。
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def is_palindrome(head):
    if head == None or head.next == None:
        return True

    slow_node = head
    fast_node = head

    # slow_node去到链表中点
    # and 前后不能调换,如果fast_node.next为None,fast_node.next.next报错
    while fast_node.next != None and fast_node.next.next != None:
        fast_node = fast_node.next.next
        slow_node = slow_node.next

    # 反转后半部分链表
    pointed_to_node = slow_node
    changed_node = slow_node.next
    slow_node.next = None
    while changed_node != None:
        next_to_be_changed_node = changed_node.next
        changed_node.next = pointed_to_node
        pointed_to_node = changed_node
        changed_node = next_to_be_changed_node

    # 从头和从尾往中点遍历
    end = pointed_to_node
    while head.next != None:
        if head.value != end.value:
            return False
        head = head.next
        end = end.next
    return True


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    print is_palindrome(head)
