# coding: utf-8

"""
199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""
from DSD.tree.build_tree01 import gen_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        使用层序遍历，并只保留每层最后一个节点的值
        """
        if not root:
            return []
        root = gen_tree(root)
        q = []
        res = []
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level[-1])
        return res

    def dfs(self):
        pass


def test():
    r = [1,2]
    print Solution().rightSideView(r)


if __name__ == '__main__':
    test()
