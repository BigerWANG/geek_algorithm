# coding: utf-8

"""
33. 搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
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
            return -1
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            # TODO：判断左右是否有序时，头和尾是固定的
            if nums[0] <= nums[mid]:  # 如果左半部分有序
                if nums[0] <= target <= nums[mid]:  # 检查target是否在左边部分里
                    end = mid - 1  # 如果在左半部分里，那么就把区间设置在左半部分。
                else:
                    start = mid + 1 # 如果不在左半部分，那么就把区间设置在右半部分

            elif nums[0] > nums[mid]:  # 如果左半部分无序，那么右边就是有序的
                if nums[mid] <= target <= nums[len(nums) - 1]:  # 如果target在右半部分中
                    start = mid + 1  # 把搜索区间设置在右半部分中
                else:
                    end = mid - 1  # 否则就把区间设置在左半部分中
        return -1


    def _search(self, nums, target):
        """
        官方题解
        :return:
        """
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    start = mid + 1
                else:
                    end= mid - 1
        return -1





if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    s = Solution().search(nums, target)
    print(s)





