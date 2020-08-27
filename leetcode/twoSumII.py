# coding: utf-8

"""
167. 两数之和 II - 输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) <= 1:
            return []


        start, end = 0, len(numbers) - 1
        # 在剩余的元素中二分查找num2
        while start <= end:
            # 因为是递增的数组，所以可以用夹逼法，大于 target end往左移，小于targe, start往右移
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return start, end



if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 18
    print(Solution().twoSum(numbers, target))




