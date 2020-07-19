# coding: utf-8

"""
设计一个LRU缓存

运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 
进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？
"""


class CacheNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next_node = None


class LRUCache(object):

    """
    字典加双向循环链表
    使用字典存储节点，使用head和tail维护一个双向链表
    关键的两个方法：
    1，从双向链表中删除指定节点 (链表满了或者将其中的值放入链表头)
    2, 将一个节点插入到双向链表开头
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # 构建一个容量为capacity的缓存池
        self.dic = {}
        self.head = CacheNode(None, None)
        self.tail = CacheNode(None, None)
        self.head.next_node = self.tail # 双向循环链表
        self.tail.prev = self.head

        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.delete(node)
        self.insert(node)
        return node.value

    def delete(self, node):
        node.prev.next_node = node.next_node
        node.next_node = node.prev

    def insert(self, node):
        node.next_node = self.head.next_node
        node.prev = self.head
        temp = self.head.next_node
        self.head.next_node = node
        temp.prev = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            self.delete(node)
            self.insert(node)
            return
        if len(self.dic) == self.capacity:
            node = self.tail.prev
            self.delete(node)
            del self.dic[node.key]
        node = CacheNode(key, value)
        self.dic[key] = node
        self.insert(node)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

