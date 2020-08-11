# coding: utf-8

"""
验证二叉搜索树

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""

class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True

    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     nums.sort()
    #     res, k = [], 0
    #     for k in range(len(nums) - 2):
    #         if nums[k] > 0:
    #             break
    #         if k > 0 and nums[k] == nums[k - 1]:
    #             continue
    #         i, j = k+1, len(nums) - 1
    #         while i < j:
    #             s = nums[k] + nums[i] + nums[j]
    #             if s < 0:
    #                 i += 1
    #                 while i < j and nums[i] == nums[i - 1]: i += 1
    #             elif s > 0:
    #                 j -= 1
    #                 while i < j and nums[i] == nums[j - 1]: j -= 1
    #             else:
    #                 res.append([nums[k], nums[i], nums[j]])
    #                 i += 1
    #                 j -= 1
    #                 while i < j and nums[i] == nums[i - 1]: i += 1
    #                 while i < j and nums[i] == nums[j - 1]: j -= 1
    #     return res






def test():
    s = Solution()
    print s.isValidBST([-1, 0, 1, 2, -1, -4])


if __name__ == '__main__':
    test()






