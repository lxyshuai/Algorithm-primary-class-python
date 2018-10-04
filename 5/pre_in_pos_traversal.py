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
        return None
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
        current_node = stack.pop()
        print current_node.value
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)


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
    current_node = root
    while stack or current_node:
        if current_node:
            stack.append(current_node)
            current_node = current_node.left
        else:
            current_node = stack.pop()
            print current_node.value
            current_node = current_node.right


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
    result = list()
    current_node = root
    stack.append(current_node)
    while stack:
        current_node = stack.pop()
        result.append(current_node)
        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
    while result:
        print result.pop().value


def post_order_traversal_un_recursive2(root):
    """
    后序遍历非递归实现
    @param root:
    @type root:
    @return:
    @rtype:
    """
    if not root:
        return None
    stack = list()
    last_node = root
    stack.append(last_node)
    while stack:
        current_node = stack[-1]
        # 弹出一个节点前要保证其左右节点都已弹出过
        if current_node.left != None and last_node != current_node.left and last_node != current_node.right:
            stack.append(current_node.left)
        elif current_node.right != None and last_node != current_node.right:
            stack.append(current_node.right)
        else:
            last_node = stack.pop()
            print last_node.value


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

    print "============unrecursive============="
    print "pre-order: "
    pre_order_traversal_un_recursive(head)
    print "in-order: "
    in_order_traversal_un_recursive(head)
    print "pos-order1: "
    post_order_traversal_un_recursive1(head)
    print "pos-order2: "
    post_order_traversal_un_recursive2(head)
