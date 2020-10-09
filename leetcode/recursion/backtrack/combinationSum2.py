# coding: utf-8

"""
40. 组合总和 II

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

"""

class Solution:
    @staticmethod
    def combinationSum2(candidates, target):
        """
        组合总和
        1，先排序
        2，回溯
        :param candidates:
        :param target:
        :return:
        """
        res = []
        if not candidates: return res
        candidates.sort()
        n = len(candidates)
        def dfs(start, curr_sum, curr_array):  # 定义三个变量 回溯起始点，当前组合总和，当前组合数组

            if curr_sum > target:
                return

            if curr_sum == target:
                res.append(curr_array[:])
                return

            for i in range(start, n):
                # 排除重复的数字
                # 这个地方 i>start 的意思是已经循环到以start开始的下一位了
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                curr_array.append(candidates[i])
                dfs(i+1, curr_sum+candidates[i], curr_array)
                curr_array.pop()

        dfs(0, 0, [])
        return res



candidates = [2,5,2,1,2]
target = 5

# candidates = [10,1,2,7,6,1,5]
# target = 8
res = Solution.combinationSum2(candidates, target)
print(res)













