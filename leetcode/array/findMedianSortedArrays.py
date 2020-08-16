# coding: utf-8

"""
寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

"""

class Solution(object):
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        解法1 时间复杂度 O(n+m), 空间复杂度 O(n+m)
        1. 合并数组
        2. 查找中位数
        """

        merge_list = self.merge(nums1, nums2)
        l = len(merge_list)
        if l % 2 == 0:
            # 是偶数个，取中间的两个数的平均数
            return (merge_list[l // 2 - 1] + merge_list[l // 2]) / 2
        else:
            # 是奇数个，取中间数
            return merge_list[l // 2]



    def merge(self, n1, n2):
        merge_list = []
        i, j = 0, 0
        l1, l2 = len(n1), len(n2)
        while i < l1 and j < l2:
            if n1[i] <= n2[j]:
                merge_list.append(n1[i])
                i += 1
            else:
                merge_list.append(n2[j])
                j += 1

        if i < l1:
            merge_list.extend(n1[i:])
        if j < l2:
            merge_list.extend(n2[j:])
        return merge_list

    def findMedianSortedArrays2(self, nums1, nums2):
        pass


def test():
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))



if __name__ == '__main__':
    test()
