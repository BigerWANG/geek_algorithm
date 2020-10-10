# coding: utf-8

"""
52.最大子序和

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        动态规划：
        当上一个位置的数字大于0时，把当前位置数与上一个位置数相加，并更新到当前位置
        """
        n = len(nums)

        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        print(nums)
        return max(nums)


def max_sub_array(nums):
    """
    算法
    定义两个变量
    sum: 当前连续最大子数组的和
    ans: 返回结果
    如果sum > 0，则说明sum对结果有增益效果，则保留结果并加上当前遍历数字
    如果sum <= 0 ，则说明sum对结果无增益效果，需要舍弃，则sum直接更新为当前遍历数字
    每次比较sum和ans的大小，将最大值设置为ans, 遍历完成返回结果
    """
    ans = nums[0]  # 当前值
    _sum = 0  # 当前连续子数组的值
    n = len(nums)
    for i in range(n):
        if _sum > 0:
            _sum += nums[i]
        else:
            _sum = nums[i]
        ans = max(_sum, ans)

    return ans



nums = [-2, 1, -3, 4, -1, 2]
print(Solution().maxSubArray(nums))