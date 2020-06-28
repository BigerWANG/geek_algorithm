# coding: utf-8

"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。


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
        二叉搜索树的特点：
        对于节点a:
        a.left.val < a.val < a.right.val
        """

        if not root:
            return None
        
        while root:
            if root.val > p.val and root.val > q.val:  # 如果根节点大于p 和 q 那么p 和q 就在根节点的左子树
                root = root.left
            elif root.val < p.val and root.val < q.val:  # 如果根节点小于p 和 q 那么p 和q 就在根节点的右子树
                root = root.right
            else:  # 如果以上条件都不成立，那么就说明 p 和q一个大于根节点一个小于根节点，那么它们一个在root的左子树 ，一个在右子树，公共祖先只能是root
                break
        return root




def test():
    
    pass