# coding: utf-8

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        快慢指针：
        快指针先走n步伐，慢指针再走
        当快指针走到尾时，慢指针指向的节点就是要删除节点的前驱节点
        """
        fast = head
        slow = head

        for _ in range(n):
            if fast.next:
                fast = fast.next  # 快指针先走N步伐
            else:
                return head.next  # 如果n是1，那就返回head.next
        while fast.next:  # 快指针走完后，继续和慢指针同时走，直到走到结束
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next  # 此时的slow就是要删除的倒数第N个节点的前驱节点
        return head
