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


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        n中子元素的长度为K
        """
        res = []
        # 先生成数组
        nums = [i for i in range(1, n+1)]
        print(nums)

        # 使用回溯法

        def backtrack(nums_b, curr_res, index):
            print("curr_res:", curr_res)
            if len(curr_res) == k:
                # 终止条件 每个子数组的长度不能超过k
                res.append(curr_res[:])
                return

            for i in range(index, n):
                print(i, nums_b)
                curr_res.append(i)
                backtrack(nums_b[index:], curr_res, i+1)  # 回溯
                curr_res.pop()

        # 特殊情况处理
        if n == 0 or k == 0:
            return res
        backtrack(nums, [], 0)
        return res

class Solution1:
    """正确的做法"""
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


class Solution2:
    def combine(self, n,k):
        """
        正确的做法
        :param n:
        :param k:
        :return:
        """
        if k  > n:
            return []
        res = []
        nums = [i for i in range(1, n+1)]
        def dfs(nums, track):
            if len(track) == k:
                res.append(track[:])
                return

            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                dfs(nums[i:], track)  # 本题不考虑已经组合过的数字，所以这里使用切片过滤掉已经组合过的
                track.pop()
        dfs(nums, [])
        return res



if __name__ == '__main__':
    s = Solution2()
    res = s.combine(4,2)
    print(res)

