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

        def dfs(nums, size, depth, track, used, res):
            if depth == size:  # 递归到最深度就返回
                res.append(track.copy())
                return
            for i in range(size):
                if not used[i]:
                    # 检查：如果当前元素等于上一个元素并且已经被使用过，那么就跳过这次循环
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:continue
                used[i] = True
                track.append(nums[i])
                dfs(nums, size, depth+1, track, used, res)
                used[i] = False
                track.pop()
        size = len(nums)
        nums.sort()
        used = [False] * len(nums)
        res = []
        dfs(nums, size, 0, [], used, res)
        return res





nums = [1,1,2]
r = Solution().permuteUnique(nums)
print(r)