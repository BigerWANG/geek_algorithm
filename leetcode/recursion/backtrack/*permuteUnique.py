# coding: utf-8

"""

47. 全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    # 如果不是起始位置 并且当前数等于下一个数，并且上一个数没有被使用过
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

        size = len(nums)
        nums.sort()
        used = [False] * size
        res = []
        dfs(nums, size, 0, [], used, res)
        return res



nums = [1,1,2]
r = Solution().permuteUnique(nums)
print(r)