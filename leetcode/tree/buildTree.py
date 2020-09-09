# coding: utf-8

"""

105 从前序与中序遍历序列构造二叉树

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

[1,2,3]
[2,3,1]


        1
       /
      2
       \
        3

"""


from DSD.tree.build_tree01 import TreeNode


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        先确定根节点：根节点是前序遍历的第一个元素
        再在中序遍历中确定左右子树的个数：根节点左边是左子树，根节点右边是右子树
        递归这个过程
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        val = preorder.pop(0)
        root_node = TreeNode(val)
        root_index = inorder.index(val)

        left_pre = preorder[:root_index]
        left_in = inorder[:root_index]

        right_pre = preorder[root_index:]
        right_in = inorder[root_index+1:]

        root_node.left = self.buildTree(left_pre, left_in)
        root_node.right = self.buildTree(right_pre, right_in)
        return root_node

    def buildTree1(self, preorder, inorder):
        """
        力扣官方解法
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 辅助函数参数：前序遍历起始点， 前序遍历终止点，中序遍历起始点，中序遍历终止点
        def mybuild(preorder_left, preorder_right, inorder_left, inorder_right):

            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left

            # 在中序遍历中确定根节点
            inorder_root = index[preorder[preorder_root]]


            # 先把根节点建立出来（前序遍历的第一个节点就是根节点）
            root = TreeNode(preorder[preorder_root])

            # 左子树的节点个数（根节点在后续遍历中的index - 后续遍历的起始位置）
            size_left_subtree = inorder_root - inorder_left

            # 构建左子树
            root.left = mybuild(preorder_left + 1,  # 前序遍历中的左子树
                                preorder_left + size_left_subtree,  # 前序遍历中左子树的终止位置
                                inorder_left,  # 中序遍历中的左子树
                                inorder_root - 1)  # 中序遍历中左子树终止位置

            # 构建右子树
            root.right = mybuild(preorder_left + size_left_subtree + 1,  # 前序遍历中的右子树起始点
                                 preorder_right,  # 前序遍历中右子树的终止点
                                 inorder_root + 1,  # 中序遍历中右子树的起始点
                                 inorder_right)  # 中序遍历中右子树的终止点
            return root
        n = len(preorder)
        # 构造哈希映射，快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}  # 把中序遍历序列映射成一个字典方便递归函数查找
        return mybuild(0, n-1, 0, n-1)



s = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
tree1 = s.buildTree(preorder, inorder)





# print(tree.left.left)
print(">>>>>>>")