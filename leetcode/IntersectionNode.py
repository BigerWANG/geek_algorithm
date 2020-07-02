# coding: utf8

"""
相交链表
我来到你的城市，走过你来时的路


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNodeBySet(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        使用集合保存第一个链表
        再遍历B查看B中的元素是否在集合中，如果存在返回
        """
        if not headA or not headB:
            return None
        S = set()
        ha, hb = headA, headB
        while ha:
            S.add(headA)
            ha = ha.next
        while hb:
            if hb in S:
                return hb
            headB = headB.next
        return None

    def getIntersectionNodeByTwoIndex(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        使用双指针
        ha和hb分别指向headA和headB
        ha和hb每次同时向前走一步，如果走到头 就指向对方的头结点继续走
        直到相遇
        如果两个一直没有相遇，最后就会都指向空节点 退出循环
        """
        ha, hb = headA, headB
        while ha != hb:  #
            ha = ha.next if ha else headB  # 如果ha走到头，ha指向headB继续走
            hb = hb.next if hb else headA  # 如果hb走到头，hb指向headA继续走
        return ha



