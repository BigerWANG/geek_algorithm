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

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        temp = []
        def recursion(idx, res):
            if idx >= len(candidates) or res >= target:
                if res == target:
                    ans.append(temp[:])
                return

            temp.append(candidates[idx])
            recursion(idx, res + candidates[idx])
            temp.pop()
            recursion(idx + 1, res)

        recursion(0, 0)
        return ans


class Solution1:
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp): # 回溯函数：参数：（候选数组下标，当前组合的总数，当前组合数组）
            if tmp_sum > target or i == n:  # 剪枝：如果当前组合总数大于目标数或者已经遍历完了，直接 return 不添加tmp到res中
                return
            if tmp_sum == target:  # 如果
                res.append(tmp)
                return
            # i是起始高度，j是当前index
            for j in range(i, n): # 这里循环多少次就是递归多少次，在回溯中递归深度不能大于决策树高度
                if tmp_sum + candidates[j] > target:  # 一旦大于这个数就退出循环停止迭代
                    break
                backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])
        backtrack(0, 0, [])
        return res




class Solution2(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        track 长度 <= k
        """

        res = []
        if n < 1:
            return []

        nums = list(range(1, n+1))

        def dfs(nums, track):
            if len(track) == k:
                res.append(track[:])
                return
            else:
                for i in range(len(nums)):
                    if nums[i] in track:
                        continue
                    track.append(nums[i])
                    dfs(nums[i:], track)
                    track.pop()
        dfs(nums, [])
        return res


class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        找出nums所有的子集
        """
        res = []
        def dfs(start, track):
            if k == len(track):
                res.append(track[:])
                return

            for i in range(start, len(nums)):
                track.append(nums[i])
                dfs(i + 1, track)  #
                track.pop()
        for k in range(len(nums)+1):
            dfs(0, [])
        return res





s = Solution3()
res = s.subsets([1,2,3])
print(res)













