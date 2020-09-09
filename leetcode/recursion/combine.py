# coding: utf-8
"""


给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


# class Solution(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         n中子元素的长度为K
#         """
#         res = []
#         # 先生成数组
#         nums = [i for i in range(1, n+1)]
#         print(nums)
#
#         # 使用回溯法
#
#         def backtrack(nums_b, curr_res, index):
#             print("curr_res:", curr_res)
#             if len(curr_res) == k:
#                 # 终止条件 每个子数组的长度不能超过k
#                 res.append(curr_res[:])
#                 return
#
#             for i in range(index, n):
#                 print(i, nums_b)
#                 curr_res.append(i)
#                 backtrack(nums_b[index:], curr_res, i+1)  # 回溯
#                 curr_res.pop()
#
#         # 特殊情况处理
#         if n == 0 or k == 0:
#             return res
#         backtrack(nums, [], 0)
#         return res

class Soultion1:
    def combine(self, n, k):
        ans = []
        def backtarck(tmp, index):
            if len(tmp) == k:
                ans.append(tmp[:])
                return
            for i in range(index, n + 1):
                tmp.append(i)
                backtarck(tmp, i+1)
                tmp.pop()
        backtarck([], 1)
        return ans


class Soultion2:
    def combine(self, n,k):
        if k  > n:
            return []
        res = []
        def dfs(nums, track):
            if len(track) == k:
                res.append(track[:])
                return

            for i in nums:
                if i in track:
                    continue
                track.append(i)
                dfs(nums, track)
                track.pop()
        nums = [i for i in range(1, n+1)]
        dfs(nums, [])
        return res



if __name__ == '__main__':
    s = Soultion2()
    res = s.combine(4,2)
    print(res)

