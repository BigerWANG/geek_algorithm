# coding: utf-8

"""
从尾到头打印链表
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def recursion_reverse(self, head):
        """
        递归法：
        递推阶段 每次传入 head.next， 以head==none为递归终止条件
        """
        if head:
            return self.recursion_reverse(head.next) + [head.val]
        else:
            return []

    def stack_reverse(self, head):
        """
        使用辅助栈：
        先遍历一遍链表，元素全部入栈
        再依次出栈就完了
        """


def test():
    pass

if __name__ == '__main__':
    test()
