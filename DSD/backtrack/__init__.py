# coding: utf-8

"""
回溯算法

解决一个回溯问题，实际上是对一个决策树的遍历过程

确定三点：
1.路径：也就是已经做出的选择
2.选择列表： 也就是你当前可以做出的选择
3.结束条件：也就是达到决策树底层，无法再做出选择的条件


回溯算法代码框架：

result = []

def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择

核心是for循环中的递归，在递归调用之前 做选择，在递归调用之后 撤销选择

"""
from copy import copy

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    if not nums:
        return []
    res = []

    # t路径： 记录在track中
    def backtrack(nums, track):
        # 结束条件：nums中的元素全都在track中出现
        if len(track) == len(nums):
            res.append(copy(track))
            return
        for i in nums:
            # 选择列表：nums中不存在与tack的那些元素
            if i in track:
                continue
            # 做选择：添加到track中
            track.append(i)
            # 进入下一层决策树
            backtrack(nums, track)
            # 取消选择
            track.pop()
    backtrack(nums, []4)
    return res



res = permute([1,2,3,4])
print(res)
print(len(res))
