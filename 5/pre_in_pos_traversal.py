# coding=utf-8
"""
二叉树先序、中序，后序遍历的非递归,递归实现
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def pre_order_traversal_recursive(root):
    """
    先序遍历递归实现
    @param root:
    @type root:
    @return:
    @rtype:
    """
    if not root:
        return
    print root.value
    pre_order_traversal_recursive(root.left)
    pre_order_traversal_recursive(root.right)


def pre_order_traversal_un_recursive(root):
    """
    先序遍历非递归实现
    @param root:
    @type root:
    @return:
    @rtype:
    """
    if not root:
        return
    stack = list()
    stack.append(root)
    while stack:
        middle = stack.pop()
        print middle.value
        if middle.right:
            stack.append(middle.right)
        if middle.left:
            stack.append(middle.left)


def in_order_traversal_recursive(root):
    """
    中序遍历递归实现
    @param root:
    @type root:
    @return:
    @rtype:
    """
    if not root:
        return
    in_order_traversal_recursive(root.left)
    print root.value
    in_order_traversal_recursive(root.right)


def in_order_traversal_un_recursive(root):
    """
    中序遍历非递归实现
    @param root:
    @type root:
    @return:
    @rtype:
    """
    if not root:
        return
    stack = list()
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print root.value
            root = root.right


def post_order_traversal_recursive(root):
    """
    后序遍历递归实现
    @param root:
    @type root:
    @return:
    @rtype:
    """
    if not root:
        return
    post_order_traversal_recursive(root.left)
    post_order_traversal_recursive(root.right)
    print root.value


def post_order_traversal_un_recursive1(root):
    """
    后序遍历非递归实现
    @param root:
    @type root:
    @return:
    @rtype:
    """
    if not root:
        return
    stack = list()
    help = list()
    stack.append(root)
    while stack:
        middle = stack.pop()
        help.append(middle)
        if middle.left:
            stack.append(middle.left)
        if middle.right:
            stack.append(middle.right)
    while help:
        print help.pop().value


def post_order_traversal_un_recursive2(root):
    """
    后序遍历非递归实现
    @param root:
    @type root:
    @return:
    @rtype:
    """
    if not root:
        return
    stack = list()
    stack.append(root)

    while stack:
        current_node = stack[-1]
        # 判断该节点左子节点已入栈并出栈
        if current_node.left != None and root != current_node.left and root != current_node.right:
            stack.append(current_node.left)
        elif current_node.right != None and root != current_node.right:
            stack.append(current_node.right)
        else:
            print stack.pop().value
            root = current_node


if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    head.left.left = Node(2)
    head.left.right = Node(4)
    head.left.left.left = Node(1)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.right = Node(10)
    head.right.right.left = Node(9)
    head.right.right.right = Node(11)

    print "==============recursive=============="
    print "pre-order: "
    pre_order_traversal_recursive(head)
    print "in-order: "
    in_order_traversal_recursive(head)
    print "pos-order: "
    post_order_traversal_recursive(head)
    #
    # print "============unrecursive============="
    print "pre-order: "
    pre_order_traversal_un_recursive(head)
    print "in-order: "
    in_order_traversal_un_recursive(head)
    print "pos-order1: "
    post_order_traversal_un_recursive1(head)
    print "pos-order2: "
    post_order_traversal_un_recursive2(head)
