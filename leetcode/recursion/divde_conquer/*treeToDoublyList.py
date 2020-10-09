# coding: utf-8

"""
二叉搜索树与双向链表

将二叉搜索树转换成双向循环链表
"""



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def __init__(self):
        self.head = None  # 头结点
        self.pre = None  # 尾节点

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        算法流程：
        1， 终止条件：当节点cur为空，代表越过叶子节点，直接返回
        2，递归左子树，即dfs(cur.left)
        3, 构建链表：
            1，当pre为空时：代表正在访问链表头结点，记为head
            2, 当pre不为空时：修改双向节点引用，pre.right, cur = cur.left, pre
            3, 保存cur： 更新pre = cur，即节点cur是后继节点的pre
        4, 递归右子树：dfs(cur.left)
        """

        if not root:
            return None
        self.dfs(root)
        # 连接头尾节点
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head


    def dfs(self, cur):
        """中序遍历"""
        if not cur:
            return

        self.dfs(cur.left)
        if self.pre:
            self.pre.right = cur
            cur.left = self.pre
        else: # 记录头结点
            self.head = cur
        self.pre = cur
        self.dfs(cur.right)








