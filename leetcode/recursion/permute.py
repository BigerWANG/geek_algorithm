# coding: utf-8

"""
46. 全排列


给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return nums

        # 保存状态的track
        res = []
        def dfs(nums, track):
            if len(nums) == len(track):  # 这次排列已经结束，保存最终状态
                res.append(track[:])
                return
            for i in nums:  # 对决策树进行遍历
                if i in track: # 不重复添加
                    # 搜索策略：按顺序枚举每一位可能出现的情况，已经选择的数字在当前要选择的数字中不能出现，按照这种策略搜索就能做到不重不漏
                    continue
                track.append(i)
                dfs(nums, track)  # 递归
                track.pop() # 回溯状态
        dfs(nums, [])
        return res



res = Solution().permute(nums=[1,2,3,4,5])


print(res)