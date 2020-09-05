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
        return self.dg(root, -(2**32), 2**32)

    def dg(self, root, min_value, max_value):
        if not root:
            return True

        if not (min_value < root.val < max_value and root.val):
            return False

        if not self.dg(root.left, min_value, root.val):
            return False

        if not self.dg(root.right, root.val, max_value):
            return False

        return True














def test():
    s = Solution()
    s.isValidBST([-1, 0, 1, 2, -1, -4])


if __name__ == '__main__':
    test()


