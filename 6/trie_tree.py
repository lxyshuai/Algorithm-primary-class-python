# coding=utf-8
"""
何为前缀树？
如何生成前缀树？
例子：
一个字符串类型的数组arr1，另一个字符串类型的数组arr2。
arr2中有哪些字符，是arr1中出现的？请打印
arr2中有哪些字符，是作为arr1中某个字符串前缀出现的？请打印
"""
class TrieNode(object):
    def __init__(self):
        self.path = 0
        self.end = 0
        self.tire_nodes = dict()


class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        char_list = list(word)
        current_node = self.root
        for char in char_list:
            if not current_node.tire_nodes.get(char, False):
                current_node.tire_nodes[char] = TrieNode()
            current_node = current_node.tire_nodes[char]
            current_node.path += 1
        current_node.end += 1

    def delete(self, word):
        if not word:
            return
        if self.search(word):
            char_list = list(word)
            current_node = self.root
            for char in char_list:
                if current_node.tire_nodes.get(char).path == 1:
                    current_node.tire_nodes[char] = None
                    return
                current_node.tire_nodes[char].path -= 1
                current_node = current_node.tire_nodes[char]
            current_node.end -= 1

    def search(self, word):
        if not word:
            return
        char_list = list(word)
        current_node = self.root
        for char in char_list:
            if current_node.tire_nodes.get(char) == None:
                return False
            current_node = current_node.tire_nodes[char]
        return current_node.end != 0

    def prefix_number(self, pre):
        if not pre:
            return
        char_list = list(pre)
        current_node = self.root
        for char in char_list:
            if current_node.tire_nodes.get(char) == None:
                return 0
            current_node = current_node.tire_nodes[char]
        return current_node.path


if __name__ == '__main__':
    trie = TrieTree()
    print trie.search("zuo")
    trie.insert("zuo")
    print trie.search("zuo")
    trie.delete("zuo")
    print trie.search("zuo")
    trie.insert("zuo")
    trie.insert("zuo")
    trie.delete("zuo")
    print trie.search("zuo")
    trie.delete("zuo")
    print trie.search("zuo")
    trie.insert("zuoa")
    trie.insert("zuoac")
    trie.insert("zuoab")
    trie.insert("zuoad")
    trie.delete("zuoa")
    print trie.search("zuoa")
    print trie.prefix_number("zuo")
