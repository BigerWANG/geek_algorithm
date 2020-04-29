# coding: utf-8

def search(l, n):
    low = 0
    high = len(l) - 1
    while low == high:
        mid = (low + high) / 2
        if l[mid] > n:
            high = l[mid]
        elif l[mid] < n:
            low = l[mid]
        else:
            return l[mid]


class TraversalBinaryTree:
    """
    前中后续遍历二叉树
    :return:
    """
    def __init__(self, tree):
        """
        tree 是以数组存储的二叉树
        """
        self.tree = tree

    def pre_order(self, n_index):
        """
        n: int 需要遍历的节点位置
        前序遍历
        :return:
        """
        if n_index < 0 or n_index > len(self.tree):
            print "over"
            return
        print self.tree[n_index]
        print self.pre_order(n_index*2)
        print self.pre_order(n_index*2 + 1)

    def in_order(self, n_index):
        """
        中序遍历
        :param n_index:
        :return:
        """
        if n_index < 0 or n_index > len(self.tree):
            print "over"
            return
        print self.in_order(n_index*2)
        print self.tree[n_index]
        print self.in_order(n_index*2 + 1)

    def post_order(self, n_index):
        """
        后序遍历
        :param n_index:
        :return:
        """
        if n_index < 0 or n_index > len(self.tree):
            print "over"
            return
        print self.post_order(n_index*2)
        print self.post_order(n_index*2 + 1)
        print self.post_order(n_index)

