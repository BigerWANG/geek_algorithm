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
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp): # 回溯函数：参数：（候选数组下标，当前组合的总数，当前组合数组）
            # if tmp_sum > target or i == n:  # 剪枝：如果当前组合总数大于目标数或者已经遍历完了，直接 return 不添加tmp到res中
            #     return
            if tmp_sum == target:  # 如果
                res.append(tmp)
                return
            if i > 0 and candidates[i] == candidates[i-1]:
                return
            # i是起始高度，j是当前index
            for j in range(i, n): # 这里循环多少次就是递归多少次，在回溯中递归深度不能大于决策树高度
                if tmp_sum + candidates[j] > target:  # 一旦大于这个数就退出循环停止迭代
                    break
                backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])
        backtrack(0, 0, [])
        return res



s = Solution()
res = s.combinationSum([1,4,2,3], 5)
print(res)













