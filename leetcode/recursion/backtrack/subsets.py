# coding: utf-8

"""
78 子集

返回一个数组的子集
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        算法：
        定义一个回溯方法 backtrack(first, curr)
        第一个参数为索引 first，第二个参数为当前子集 curr

        * 如果当前子集构造完成，将它输出到集合中
        * 否则，从first到n 遍历索引i：
            将整数 nums[i] 添加到当前子集 curr
            继续递归的向子集中添加整数：backtrack(i+1, curr)
            从 curr中删除nums[i]进行回溯
        """

        if not nums:
            return []
        res = []
        def backtrack(first=0, curr=list()):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)  # 每次递归起始index往后进一位，反正重复计算
                curr.pop()

        for k in range(len(nums) + 1):  # 因为是子集，所以子集长度最大不能超过nums, 长度递增, 所以在循环中调用递归函数
            backtrack(0, [])
        return res



s = Solution()
print(s.subsets([1,2,3]))                     