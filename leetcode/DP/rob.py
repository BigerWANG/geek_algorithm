# coding: utf-8

"""
198.打家劫舍
"""

def rob(nums):
    """
    dp[i] = max(dp[i-2] + dp[i], dp[i-1])
    :param nums:
    :return:
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = nums
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    res = max(dp[0], dp[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2] + dp[i], dp[i-1])
        res = max(res, dp[i])
    return res


nums = [2, 1, 1, 2]
print rob(nums)

