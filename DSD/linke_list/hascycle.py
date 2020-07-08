# coding: utf-8

"""
给定一个链表，判断链表中是否有环

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        定义快慢指针
        快指针走一步
        慢指针走两步
        如果两个指针指向同一节点，说明有环(相遇)
        如果快指针走到头没有相遇，说明没有环
        """
        # 定义快慢指针
        if not head:
            return False
        slow = head
        fast = head.next
        while fast:
            if slow.val == fast.val:
                return True
            if not fast.next:
                break
            slow = slow.next
            fast = fast.next
        return False

    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        骚解法：
        将头节点定义成一个固定值，判断是否会再遇到这个值
        """
        if not head:
            return False
        while head:
            if head.val == "sb":
                return True
            else:
                head.val = "sb"
            head = head.next
        return False