# coding: utf-8

"""
删除链表的倒数第n个节点，并且返回链表的头结点。

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        倒数第n个节点位置：链表的长度 - n
        1, 得出链表的长度
        2，倒数第n个节点位置：链表的长度 - n
        3，得到要删除节点位置
        4，删除节点
        5，先得到要删除节点的前驱节点 然后将前驱节点next=要删除节点的next
        6, 返回head
        """
        if not head:
            return None
        l = 0
        while head:
            head = head.next
            l += 1
        remove_node_index = l - n
        if remove_node_index > 0:
            while True:
                head = head.next
                remove_node_index -= 1
                if not remove_node_index:
                    remove_node_node = head
                    break
            while head.next:
                head = head.next
                if head.next.val == remove_node_node.val:
                    head.next = remove_node_node.next
                    remove_node_node.next = None

        return head

