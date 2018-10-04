# coding=utf-8
"""
在二叉树中找到一个节点的后继节点
【题目】
现在有一种新的二叉树节点类型如下：
public class Node {
    public int value
    public Node left
    public Node right
    public Node parent
    public Node(int data) {
    this.value = data
    }
}
该结构比普通二叉树节点结构多了一个指向父节点的parent指针。假设有一
棵Node类型的节点组成的二叉树，树中每个节点的parent指针都正确地指向
自己的父节点，头节点的parent指向null。只给一个在二叉树中的某个节点
node，请实现返回node的后继节点的函数。在二叉树的中序遍历的序列中，
node的下一个节点叫作node的后继节点。
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def get_next_node(node):
    if not node:
        return node
    # 第一种情况,该节点有右子树,该节点的后继节点为右子树的最左节点
    if node.right != None:
        current_node = node.right
        while current_node.left:
            current_node = current_node.left
        return current_node
    # 第二种情况,该节点没有右子树,找到某个祖先节点使该节点位于该祖先节点的左子树,如果没有遍历到root则返回None
    else:
        parent = node.parent
        while parent and parent.left != node:
            node = parent
            parent = node.parent
        return parent


if __name__ == '__main__':
    head = Node(6)
    head.parent = None
    head.left = Node(3)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    test = head.left.left
    print str(test.value) + " next: " + str(get_next_node(test).value)
    test = head.left.left.right
    print str(test.value) + " next: " + str(get_next_node(test).value)
    test = head.left
    print str(test.value) + " next: " + str(get_next_node(test).value)
    test = head.left.right
    print str(test.value) + " next: " + str(get_next_node(test).value)
    test = head.left.right.right
    print str(test.value) + " next: " + str(get_next_node(test).value)
    test = head
    print str(test.value) + " next: " + str(get_next_node(test).value)
    test = head.right.left.left
    print str(test.value) + " next: " + str(get_next_node(test).value)
    test = head.right.left
    print str(test.value) + " next: " + str(get_next_node(test).value)
    test = head.right
    print str(test.value) + " next: " + str(get_next_node(test).value)
    test = head.right.right # 10's next is null
    print str(test.value) + " next: " + str(get_next_node(test))