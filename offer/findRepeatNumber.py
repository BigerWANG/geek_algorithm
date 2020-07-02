# coding: utf-8

"""


"""


class Solution(object):
    def findRepeatNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        暴力穷举
        """
        if not nums:
            return []
        res = list()
        for i in nums:
            if i in res:
                return i
            res.append(i)





def test():
    nums = [2, 3, 1, 0, 2, 5, 3]
    print Solution().findRepeatNumber1(nums)


if __name__ == '__main__':
    test()
