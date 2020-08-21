# coding: utf-8

"""
给定一个二叉树，返回其节点值自底向上的层次遍历。
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）





"""

from DSD.tree.build_tree01 import gen_tree




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        root = gen_tree(root)
        queue.append(root)
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res[::-1]


class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        层序遍历，判断每层是否是回文列表
        """
        if not root:
            return []
        queue = []
        root = gen_tree(root)
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level != level[::-1]:
                return False
        return True





def test():
    print(Solution1().isSymmetric([1,2,2,3,4,4,3]))

if __name__ == '__main__':
    test()