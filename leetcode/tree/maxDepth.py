# coding: utf-8

"""

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        最大深度 = max(左子树深度，右子树深度) + 根节点
        """
        if not root:
            return 0
        deep = 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + deep