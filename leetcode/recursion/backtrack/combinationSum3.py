# coding: utf-8

"""
216. 组合总和 III
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

"""


class Solution(object):
    @staticmethod
    def combinationSum3(k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if not k: return []

        candidates = range(1, 10)
        candidates = list(candidates)  # py3需要加这一句

        _len = len(candidates)

        res = []
        def dfs(start, curr_sum, curr_array):

            if curr_sum > n:
                return

            if curr_sum == n and len(curr_array) == k:
                res.append(curr_array[:])
                return

            for i in range(start, _len):
                curr_array.append(candidates[i])
                dfs(i+1, curr_sum + candidates[i], curr_array)
                curr_array.pop()

        dfs(0, 0, [])

        return res





k = 3
n = 9



res= Solution.combinationSum3(k, n)
print(res)