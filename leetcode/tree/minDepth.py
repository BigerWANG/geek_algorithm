# coding: utf-8

"""

二叉树的最小深度

返回最小的子树
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        最小深度 = min(左子树深度，右子树深度) + 根节点
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left:
            return right + 1
        if not root.right:
            return left + 1
        return min(left, right) + 1
