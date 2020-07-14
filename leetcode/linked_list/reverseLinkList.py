# coding: utf-8

"""
反转链表
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        双指针：
        pre(前驱指针))指向Null
        cur（当前指针）指向head
        每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
        """
        pre = None  # 指定一个前驱节点为空
        cur = head  # 当前节点
        while cur:
            _next = cur.next  # 先算出来下一个节点保存在变量中
            cur.next = pre  # 当前节点指向前驱节点，（反转）
            pre = cur  # pre向前挪一位
            cur = _next  # 当前节点向前挪一位
        return pre


def test():
    pass


if __name__ == '__main__':
    test()

