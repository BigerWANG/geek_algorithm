# coding: utf-8

"""

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""


from DSD.tree.build_tree01 import TreeNode





class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        前序遍历 root, left, right
        先构造根节点
        再构造左子树
        再构造右子树
        把左子树和右子树关联到根节点
        """
        if not preorder or not inorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        root_index = inorder.index(val)
        root.left = self.buildTree(preorder[:root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index:], inorder[root_index+1:])
        return root

def test():
    preorder = [1,2,3]
    inorder = [2,3,1]
    root = Solution().buildTree(preorder, inorder)

    print(root.left)
    print(root.left.left)
    print(root.left.right)


if __name__ == '__main__':
    test()