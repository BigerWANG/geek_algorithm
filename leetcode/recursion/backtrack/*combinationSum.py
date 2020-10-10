# coding: utf-8

"""
39. 组合总和


给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

提示1：

候选数组里有2, 如果找到了组合总数为7-2 = 5的所有组合，再在之前加上2，就是7的所有组合
同理考虑3，如果找到了组合总和为7-3=4的所有组合，再在之前加上3，就是 7 的所有组合
以此类推

"""


class Solution:
    @staticmethod
    def combinationSum(candidates, target):
        res = []
        if not candidates: return []
        n  = len(candidates)
        def dfs(start, curr_sum, curr_array):
            if start > n:
                return

            if curr_sum > target:  # 这一步很关键, 如果不判断则会栈溢出
                return

            if curr_sum == target:
                res.append(curr_array[:])
                return

            for i in range(start, n):
                curr_array.append(candidates[i])
                dfs(i, candidates[i] + curr_sum, curr_array)
                curr_array.pop()
        dfs(0, 0, [])
        return res





candidates = [2,3,5]
target = 8
res = Solution.combinationSum(candidates, target)
print(res)
