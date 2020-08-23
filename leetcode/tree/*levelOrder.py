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

    def levelOrder1(self, root):
        """
        :param root:
        :return:
        """
        if not root:
            return []
        from collections import deque
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
