# coding: utf-8

"""
根据array生产二叉树
"""

from collections import deque


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "<Node {}>".format(self.val)

    def preorder(self):
        if self.val is not None:
            print(self.val)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.val is not None:
            print(self.val)
        if self.right is not None:
            self.right.inorder()


def gen_tree(array):
    """
    利用生成器将数组转化成树对象
    """
    if not array:
        return None

    iter_value = iter(array)  # 转换成一个生成器
    root = TreeNode(next(iter_value))  # 取第一个就是根节点
    d = deque()
    d.append(root)
    while True:
        head = d.popleft()  # 把刚入队的节点从左边取出来，并循环这个过程
        try:
            head.left = TreeNode(next(iter_value))  # 取下一个节点，就是左子节点
            d.append(head.left)  # 左子节点入队
            head.right = TreeNode(next(iter_value)) # 再下一个就是右子节点
            d.append(head.right)  # 右子节点入队
        except StopIteration:  # 直到生成器为空，取不出来下一个节点为止
            break
    return root


def pre_traverse_tree(node):
    if node is None:
        return
    yield pre_traverse_tree(node.left)
    yield pre_traverse_tree(node.right)
    yield node.val



l = [4,2,7,1,3,6,9]

root = gen_tree(l)


class Solution(object):
    def invertTree(self, root):
        """
        翻转二叉树
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 终止条件
        if not root:
            return root
        # 处理当前逻辑层
        root.left, root.right = root.right, root.left
        # 下探到下一层
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root





def dfs(root):
    if not root:
        return None
    q = []






