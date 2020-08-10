# coding: utf-8

"""
98. 验证二叉搜索树

判断一棵树是不是二叉搜索树

BST：root.left < root < root.right

方法：递归判断

递推公式：
f(n)

终止条件：
递归到叶子节点
not root: return True
遇到不符合BST特性时
not (root.left < root < root.right): return False

"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not (root.left < root < root.right):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)




def test():
    pass



if __name__ == '__main__':
    test()