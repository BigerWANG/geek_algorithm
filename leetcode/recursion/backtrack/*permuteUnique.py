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

        



class Solution1(object):
    def permuteUnique(self, nums):
        """
        :param nums:
        :return:
        """
        from collections import Counter

        def track(path, counter):
            if len(path) == len(nums):
                res.append(path[:])

            for x in counter:
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    track(path, counter)
                    path.pop()
                    counter[x] += 1
        res = []
        track([], Counter(nums))
        return res




nums = [1,1,2]
r = Solution1().permuteUnique(nums)
print(r)