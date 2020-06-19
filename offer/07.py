# coding: utf-8

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        preorder: root > left > right
        inorder: left > root > right
        afterorder: right > left > root
        """
        if not preorder or inorder:
            return []





def test():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

if __name__ == '__main__':
    test()
