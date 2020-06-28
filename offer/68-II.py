# coding: utf-8

"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8, None, None,7,4]
                  3
               /    \
              5      1
            /  \    /  \
           6    2  0    8
               / \
              7   4


所有节点都是唯一的
p, q 均存在于树中
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        1，递归左子树和右子树, 查找节点p和q

        2，在左子树中查找p或q，查到就返回

        3，如果左子树和右子树都是空，则说明没找到p或q， 直接return None

        4，如果右子树中存在，左子树不存在，说明在右子树中，return 右子树

        5，如果左子树存在，右子树不存在，说明在左子树中，return 左子树

        6，如果左右子树都不为空，则说明p 和 q分别在左右子树中，那么最近公共祖先就是root

        """
        if not root:
            return None
        if root == p or root == q:  # 终止递归条件
            return root
        # 分别递归左右两个子树，查询到p或q就结束递归，返回p或q的父节点
        left = self.lowestCommonAncestor(root.left, p, q)  # 因为是递归，所以假设此时已经找到了最终结果
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果右子树为空，则说明结果在左子树中
        if left and not right:
            return left
        # 同上 如果左子树中不存在 p或 q 那么返回返回右子树
        if right and not left:
            return right
        # 如果左右子树都存在，那么公共祖先就只能是root节点
        if right and left:
            return root





def test():
    
    pass