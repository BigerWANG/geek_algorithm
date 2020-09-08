# coding: utf-8

"""
236. 二叉树的最近公共祖先


给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

"""
from DSD.tree.build_tree01 import gen_tree, TreeNode



class Solution(object):
    def __init__(self):
        self.ans = None


    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, p, q):
            """辅助函数"""
            # 终止条件
            if not root:
                return False
            # 分别递归左子树和右子树
            is_left = dfs(root.left, p, q)
            is_right = dfs(root.right, p, q)

            # 判断条件：
            # 如果左子树和右子树分别存在p或q,
            # 或者root节点等于p或者q并且p或者q的其中一个节点存在于左子树或右子树中
            if ((is_left and is_right) or
                    ((root.val == p.val or root.val == q.val) and (is_left or is_right))):
                # 满足以上条件后，说明找到了公共节点，把这个节点保存到ans变量中
                self.ans = root

            # 返回结果判断：
            # p或q存在于左子树或右子树，或者根节点等于p或者等于q
            return (is_left or is_right) or (root.val == p.val or root.val == q.val)
        dfs(root, p, q)
        return self.ans




if __name__ == '__main__':
    l = [3,5,1,6,2,0,8,None,None,7,4]
    s = Solution()
    root = gen_tree(l)
    print(s.lowestCommonAncestor(root, TreeNode(1), TreeNode(8)))
