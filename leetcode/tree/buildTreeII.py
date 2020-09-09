# coding: utf-8

"""
106. 从中序与后序遍历序列构造二叉树
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""

from DSD.tree.build_tree01 import TreeNode

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        后续遍历 根节点在后续遍历的最后一个位置
        """
        if not inorder or not postorder:
            return None
        # 先找出来根节点的值
        val = postorder.pop()
        # 在中序遍历中划分左子树与右子树
        root_index = inorder.index(val)
        root = TreeNode(val)
        left_in = inorder[:root_index]
        left_post = postorder[:root_index]

        right_in = inorder[root_index + 1:]
        right_post = postorder[root_index:]

        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)

        return root




