# coding: utf-8

"""
81. 搜索旋转排序数组 II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        算法：
        如果 [l, mid - 1] 是有序数组，
        且 target 的大小满足 nums[l] <= target <= nums[mid - 1]，则我们应该将搜索范围缩小至 [l, mid - 1]，否则在 [mid + 1, r] 中寻找。
        如果 [mid, r] 是有序数组，且 target 的大小满足 nums[mid+1] <= target <= nums[r]，则我们应该将搜索范围缩小至 [mid + 1, r]，否则在 [l, mid - 1] 中寻找。
        """
        if not nums:
            return False
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            if nums[start] == nums[mid]:  # 如果中间数等于开始数，那么就pass掉第一个数
                start += 1
                continue

            if nums[0] < nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[0] >= nums[mid]:
                if nums[mid] <= target <= nums[len(nums) -  1]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False




if __name__ == '__main__':
    nums = [1,0,1,1,1]
    target = 0
    s = Solution().search(nums, target)
    print(s)





