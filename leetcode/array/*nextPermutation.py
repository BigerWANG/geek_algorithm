# coding: utf-8

"""
下一个排列
题目解释：
简单的看就是，你把数组连成一个数，得到的结果应该是跟这个数最近且比他大的数，如果这个数已经最大，就返回组合的最小数

找出这个数组排序出的所有数中，刚好比当前数大的那个数

比如当前 nums = [1,2,3]。这个数是123，找出1，2，3这3个数字排序可能的所有数，排序后，比123大的那个数 也就是132

如果当前 nums = [3,2,1]。这就是1，2，3所有排序中最大的那个数，那么就返回1，2，3排序后所有数中最小的那个，也就是1，2，3 -> [1,2,3]
必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""


class Solution(object):
    @classmethod
    def nextPermutation(cls, nums):
        """
        :type height: List[int]
        :rtype: int
        算法需要满足以下条件：
        1, 得到一个递增的排列组合
        2，下一个数比当前数大：因此需要把后边的"大数"与当前的"小数"交换
        3，下一个数增加的幅度尽可能小：
        1）
        """





if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution.nextPermutation(nums))

