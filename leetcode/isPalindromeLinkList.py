# coding: utf-8

"""
234. 回文链表

判断一个链表是否是回文链表
示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome0(self, head):
        """
        :type head: ListNode
        :rtype: bool
        做法1 反转链表，判断两个链表是否相等
        """
        if not head:
            return True
        reverse = self.reverse(head)
        h, r = head, reverse
        while h and r:
            if h.val != r.val:
                return False
            h = h.next
            r = r.next
        return True 


    def reverse(self, head):
        if not head:
            return head
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            # 移动
            pre = cur
            cur = next
        return pre


    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        做法2：两个快慢指针，快指针走两步，慢指针走一步
        1 快指针走完时，慢指针刚好到中间，返回慢指针
        2，慢指针继续往下走
        """
        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow







