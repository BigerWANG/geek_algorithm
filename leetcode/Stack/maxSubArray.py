# coding: utf-8

"""
53. 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1，设置一个ans
        2, 设置一个变量sum保存当前值
        3，遍历数组，元素大于0的话就往后sum就累加，如果小于0的话就把它赋值给sum
        4，
        """

        ans = nums[0]
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            ans = max(ans, sum)
        return ans




def test():
    a = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print s.maxSubArray(a)

if __name__ == '__main__':
    test()