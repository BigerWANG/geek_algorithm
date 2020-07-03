# coding: utf-8

"""
判断链表是否有环

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
也就是返回环节点的上一个节点
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        return None
