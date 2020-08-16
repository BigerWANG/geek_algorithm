# coding: utf-8

"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        双指针法：
        1，先将数组排序
        2，从头开始取值h，并且定义两个指针l, r， 分别指向头的下一个元素与最后一个元素
        3，每次判断h + l +r是否等于0 分三种情况:
        1）等于0 结束
        2）小于0, l+=1, continue
        3）大于0, r-=1, continue
        注意：跳过相同的数字
        """
        # if not nums:
        #     return
        nums.sort()
        res = []
        for h in range(len(nums)): # 长度-2防止数组越界，这里要取两个指针
            if h > 0 and nums[h] == nums[h - 1]: # 注意，这里判断是否跟上一个元素重复
                continue
            l, r = h + 1, len(nums) - 1
            while l < r:
                s = sum((nums[h], nums[l], nums[r]))
                if s < 0: l += 1
                elif s > 0: r -= 1
                else:
                    res.append((nums[h], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l +=1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        # 先排序，这么做是为了方便调整两端的值并进行比较，如果<0 r向右一位，如果>0 l向左一位
        nums.sort()
        for i in range(len(nums)):
            # 当i不是0时(不是第一次循环)并且上一个值与它相等，就跳过这个值
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:  # 判断并跳过重复值
                        l += 1
                    while l < r and nums[l] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

if __name__ == '__main__':
    p = [1,-1,-1,0]
    print(Solution().threeSum(p))

