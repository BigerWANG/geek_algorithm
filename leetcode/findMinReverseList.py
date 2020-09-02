# coding: utf-8

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""


def find_min(nums):
    """
    算法1 ：
    中间节点与start作比较
    1，如果大于start：查找中间节点的右边节点 start = mid
    2，如果小于start：查找中间节点的左边节点 end = mid
    当 mid - 1 < mid 或mid + 1 > 时,说明mid是最小节点
    :param nums:
    :return:
    """
    if not nums:
        return 0

    start, end = 0, len(nums) - 1

    # 如果最后一个元素大于第一个元素，那么这个数组就是有序的，直接返回第一个元素
    if nums[start] <= nums[end]:
        return nums[0]

    while start <= end:
        mid = (start + end) // 2

        # 如果一个元素 小于他前边的数，那么它就是最小值
        if nums[mid] < nums[mid - 1]:
            return nums[mid]

        # 如果一个数大于他后边的数，那么它后边得数就是最小值
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        if nums[mid] > nums[start]:  # 在右边区间查找
            start = mid + 1
        else: # 在左边区间查找
            end = mid - 1

a = [4,5,6,7,8,9,0,1,2]
print(find_min(a))


