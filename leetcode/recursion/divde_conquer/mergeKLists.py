# coding: utf-8

"""
23. 合并K个升序链表


给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        可以递归的合并两个升序链表
        先实现一个两个链表合并的方法
        """
        if not lists:
            return []
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = (left + right) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.merge_two_list(l1, l2)


    def merge_two_list(self, l1, l2):
        """
        合并两个链表
        :param l1:
        :param l2:
        :return:
        """
        head = ListNode(0)  # 哨兵节点
        new = head
        while l1 and l2:
            if l1.val < l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next

        if l1:
            new.next = l1
        if l2:
            new.next = l2
        return head.next



class Solution1(object):
    def permute(self, nums):
        """
        重写全排列
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(nums, track):
            if len(nums) == len(track):
                res.append(track[:])
                return

            for i in nums:
                if i in track:  # 去重
                    continue
                track.append(i)
                backtrack(nums, track)
                track.pop()

        backtrack(nums, [])
        return res


class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :param candidates:
        :param target:
        :return:
        算法：
        1，利用回溯算法搜索
        """
        pass



s = Solution1()
print(s.permute([1,2,3]))