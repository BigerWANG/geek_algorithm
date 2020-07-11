# coding: utf-8

"""
判断链表是否有环

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
也就是返回环节点的第一个节点
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycleBySet(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        用一个哈希表去保存已经遍历过的节点，返回第一个重复的节点即可
        """

        if not head:
            return None
        s = set()
        while head:
            s.add(head)
            head = head.next
            if head in s:
                return head
        return None

    def detectCycleByTwoIndex(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        使用双指针
        这类题目一般都是双指针包括（寻找距离尾部第K个节点，寻找入环口，寻找公共尾部入口）
        """











