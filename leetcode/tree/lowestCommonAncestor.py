# coding: utf-8

"""
235. 二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



"""
from DSD.tree.build_tree01 import gen_tree


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
        """

        # 终止条件
        if not root:
            return None

        # 当前层逻辑,下探到下一层
        if root.val > p.val and root.val > q.val:  # 如果 根节点大于p 和 q, p和q就在根节点的左子树
            root = self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            root = self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        return root


if __name__ == '__main__':
    l = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    s = Solution()
    root = gen_tree(l)

    print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)))
