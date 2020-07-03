# coding: utf-8

"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。

2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。

"""


class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        1， 先排序
        2，如果不存在0：
            遍历列表如果相差为>1就返回False
        3，如果存在0：
            其中两个值相差>2 or Flase

        """
        if not nums:
            return False
        nums = sorted(nums)
        prev = 0
        curr = 1
        count = 0
        if 0 in nums:
            # 先查看有几个大小王
            num_0 = nums.count(0)  # 记录间隔大于2的次数， 如果超过count次返回 False
            while prev < len(nums) - 1:
                if nums[curr] - nums[prev] >= 2:
                    count += 1
                    prev += 1
                    curr += 1
                    continue
                if count > num_0:
                    return False
                if nums[curr] - nums[prev] > 1 and nums[curr] != nums[prev]:
                    return False
                prev += 1
                curr += 1

        else:
            while prev < len(nums) - 1:
                if nums[curr] - nums[prev] > 1 and nums[curr] != nums[prev]:
                    return False
                prev += 1
                curr += 1
        return True

    def isStraight1(self, nums):
        """
        1, 如果除0之外有重复，肯定不是顺子
        2，如果除0之外最大值与最小值相差大于5，不是顺子
        3，否则 无重复切最大值-最小值<5，可以拼凑成顺子
        """
        nums = [i for i in nums if i]  # 去除0值
        return len(set(nums)) == len(nums) and max(nums) - min(nums) < 5  # 去重之后的值和原来是否相等，并且最大值减最小值是否小于5











def test():
    nums = [0, 0, 2, 2, 5]
    print Solution().isStraight(nums)




if __name__ == '__main__':
    test()
