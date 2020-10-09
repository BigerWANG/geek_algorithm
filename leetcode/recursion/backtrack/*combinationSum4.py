# coding: utf-8

"""
377. 组合总和 Ⅳ

给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

请注意，顺序不同的序列被视作不同的组合。

因此输出为 7。

进阶：
如果给定的数组中含有负数会怎么样？
问题会产生什么变化？
我们需要在题目中添加什么限制来允许负数的出现？
"""


# FIXME: 用回溯会超时，需要使用动态规划

class Solution(object):
    @staticmethod
    def combinationSum4(nums, target):
        """
        :type nums: list
        :type target: int
        :rtype: List[List[int]]

        """
        res = []

        if not nums: return []
        nums.sort()
        n = len(nums)
        def dfs(start, curr_sum, curr_array):
            if start > n:
                return
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(curr_array[:])
                return
            for i in range(start, n):
                curr_array.append(nums[i])
                dfs(i, curr_sum+nums[i], curr_array)
                curr_array.pop()
        dfs(0, 0, [])
        return res



nums = [1, 2, 3]
target = 50


res= Solution.combinationSum4(nums, target)
print(res)