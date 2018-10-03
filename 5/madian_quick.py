# coding=utf-8
from __future__ import division

"""
随时找到数据流的中位数
【题目】
有一个源源不断地吐出整数的数据流，假设你有足够的空间来
保存吐出的数。请设计一个名叫MedianHolder的结构，
MedianHolder可以随时取得之前吐出所有数的中位数。
【要求】
1．如果MedianHolder已经保存了吐出的N个数，那么任意时刻
将一个新数加入到MedianHolder的过程，其时间复杂度是
O(logN)。
2．取得已经吐出的N个数整体的中位数的过程，时间复杂度为
O(1)。
"""
import Queue


class max_heap_item(object):
    def __init__(self, value):
        self.value = value

    def __cmp__(self, other):
        if self.value > other.value:
            return -1
        elif self.value < other.value:
            return 1
        else:
            return 0


class min_heap_item(object):
    def __init__(self, value):
        self.value = value

    def __cmp__(self, other):
        if self.value < other.value:
            return -1
        elif self.value > other.value:
            return 1
        else:
            return 0


class MedianHolder(object):
    def __init__(self):
        self.max_heap = Queue.PriorityQueue()
        self.min_heap = Queue.PriorityQueue()

    def modify_two_heaps_size(self):
        if self.max_heap.qsize() == self.min_heap.qsize() + 2:
            self.min_heap.put(min_heap_item(self.max_heap.get().value))
        elif self.min_heap.qsize() == self.max_heap.qsize() + 2:
            self.max_heap.put(max_heap_item(self.min_heap.get().value))

    def add_number(self, number):
        """
        大于大根堆堆顶放入小根堆
        @param number:
        @type number:
        @return:
        @rtype:
        """
        if self.max_heap.qsize() == 0:
            self.max_heap.put(max_heap_item(number))
        else:
            if number > self.max_heap.queue[0].value:
                self.min_heap.put(min_heap_item(number))
            else:
                self.max_heap.put(max_heap_item(number))
        self.modify_two_heaps_size()

    def get_median(self):
        max_heap_size = self.max_heap.qsize()
        min_heap_size = self.min_heap.qsize()
        max_heap_root = self.max_heap.queue[0]
        min_heap_root = self.min_heap.queue[0]
        if max_heap_size + min_heap_size == 0:
            return None
        if (max_heap_size + min_heap_size) % 2 == 0:
            return (max_heap_root.value + min_heap_root.value) / 2
        else:
            return max_heap_root.value if max_heap_size > min_heap_size else min_heap_root.value


if __name__ == '__main__':
    md = MedianHolder()
    md.add_number(1)
    md.add_number(2)
    md.add_number(2)
    md.add_number(4)
    print md.get_median()
