# coding: utf-8

"""
203。移除链表元素
删除链表中等于给定值 val 的所有节点。
示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        遍历链表，如果当前节点p 的 next==val
		则
		p.next = p.next.next
		p = p.next
		设置哨兵节点（哨兵节点广泛用于树和链表中，如伪头，伪尾，它是纯功能性的，通常不保存
		任何值，其主要目的是使链表标准化，如使链表永不为空，永不无头，简化插入和删除）
		这里设置哨兵节点为头节点的前驱结点 prev


        """
        if not head:
        	return None 
        sential = ListNode(0)  # 此时 sential相当于头结点的前驱节点
        sential.next = head
        pre, cur = sential, head
        while cur:
        	if cur.val == val:
        		pre.next = cur.next
        	else:
        		pre = cur
        	cur = cur.next
        return sential.next







