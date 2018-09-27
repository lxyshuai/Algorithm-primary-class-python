# coding=utf8
"""
设计RandomPool结构    
【题目】 设计一种结构，在该结构中有如下三个功能：    
insert(key)：将某个key加入到该结构，做到不重复加入。    
delete(key)：将原本在结构中的某个key移除。
getRandom()：等概率随机返回结构中的任何一个key。    
【要求】 Insert、delete和getRandom方法的时间复杂度都是O(1)
"""
import random


class RandomPool(object):
    def __init__(self):
        self.index_key_map = {}
        self.key_index_map = {}
        self.index = 0

    def insert(self, key):
        self.index_key_map[self.index] = key
        self.key_index_map[key] = self.index
        self.index += 1

    def delete(self, key):
        # 找出弹出key对应的index
        _index = self.key_index_map[key]
        # 找出最后一个插入key
        last_key = self.index_key_map[self.index - 1]
        # 在key_index_map中将最后一个插入key的index修改为弹出key的index
        self.key_index_map[last_key] = _index
        # 弹出key_index_map中key
        self.key_index_map.pop(key)
        # 在index_key_map中将弹出的key对应的index对应的key修改为最后一个的key
        self.index_key_map[_index] = last_key
        # 弹出index_key_map中最后一个插入的
        self.index_key_map.pop(self.index - 1)
        self.index -= 1

    def get_random(self):
        if self.index == 0:
            return None
        random_index = random.randint(0, self.index - 1)
        return self.index_key_map[random_index]


if __name__ == '__main__':
    random_pool = RandomPool()
    random_pool.insert('A')
    random_pool.insert('B')
    random_pool.insert('C')
    print random_pool.get_random()
    random_pool.delete('A')
    print random_pool.get_random()
