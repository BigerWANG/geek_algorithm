# coding: utf-8

"""
设计一个LFU缓存

请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。
「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

 

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

"""


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)