# coding: utf-8


class ArrayStack:
    """
    基于数组实现的顺序栈
    """
    def __init__(self):
        self.items = []  # 数组
        self.count = 0  # 栈中元素个数
        # self.max_num = 100  # 栈的大

    def pop(self):
        """
        出栈操作
        :return:
        """
        if self.count < 0:
            raise IOError
        res = self.items[-1]
        self.items -= res
        self.count -= 1
        return res

    def push(self, item):
        """
        入栈操作
        :return:
        """
        self.items.append(item)
        self.count += 1
        return "OK"


class Q:
    """
    基于数组实现的队列
    先入先出的数据结构，支持在队尾插入元素，在队头删除元素
    """
    def __init__(self):
        pass




