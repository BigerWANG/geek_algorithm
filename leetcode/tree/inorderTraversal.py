# coding: utf-8
"""
94. 二叉树的中序遍历


给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

from DSD.tree.build_tree01 import TreeNode, gen_tree

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        # 递归遍历
        """
        res = []
        def inorder(root):
            if not root:
                return root
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res



class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        # 循环遍历
        使用栈保存每个节点进行遍历
        """
        res = []
        stack = []
        curr = root  # 设置一个指向根节点的指针
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left  # 这一步是先把左子树全部入栈
            else:  # curr 为 False 说明遍历到头了，可以从栈中取节点到res里了
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right  # 取完当前节点就可以转换成右子树
        return res


root = gen_tree([1,None,2,3])
s = Solution()
res = s.inorderTraversal(root)

print(res)
