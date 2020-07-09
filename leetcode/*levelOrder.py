# coding: utf-8

"""
给定一个二叉树，返回其按层序遍历的节点值， 逐层的从左到右访问所有节点


示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<Node {}>".format(self.val)


class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        1, 先把树转换成list(前序遍历)
        2，再根据切片层序遍历

        """
        from collections import defaultdict
        d = defaultdict(list)
        def f(r, i):
            if r:
                d[i].append(r.val)
                f(r.left, i+1)
                f(r.right, i+1)
        f(root, 0)
        return [i for i in d.values()]


class Solution(object):
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        1, 先把树转换成list(前序遍历)
        2，再根据切片层序遍历

        """
        tree = self.preorder(root)
        i = 1
        level_order = []
        while i < len(tree):
            _l = [i for i in tree[i-1: i*2 - 1] if i]
            level_order.append(_l)
        return levelOrder
            

    def preorder(self, root):
        tree_list = []
        if not root:
            return tree_list
        tree_list.append(self.preorder(root))
        tree_list.append(self.preorder(root.left))
        tree_list.append(self.preorder(root.right))
        return root.val