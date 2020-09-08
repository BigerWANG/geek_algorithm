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

        在 后续遍历中找边界，
        确定前序遍历中那个区间是左子树，哪个区间是右子树，
        分别遍历构造这两个区间连接到root上就ok
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder or not inorder:
            return []

        if len(preorder) != len(inorder):
            return []

        # 先确定头结点
        r = preorder[0]
        root = TreeNode(r)
        # 剩下的节点
        r_index = inorder.index(r)  # 根节点在中序遍历中的位置
        left_tree = len(inorder[:r_index])  # 左子树长度
        # right_tree = len(inorder[r_index + 1:]) # 右子树长度

        root.left = self.init_tree(preorder[1:1+left_tree])
        root.right =self.init_tree(preorder[1+left_tree:])

        self.buildTree(preorder[1:1+left_tree], preorder[1+left_tree:])
        return root


    def init_tree(self, items):
        if not items:
            return TreeNode(None)
        l = iter(items)
        d = []
        root = TreeNode(next(l))
        d.append(root)
        while d:
            node = d.pop(0)
            try:
                node.left = TreeNode(next(l))
                d.append(node.left)
                node.right = TreeNode(next(l))
                d.append(node.right)
            except StopIteration:
                break
        return root


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

            print(inorder_root)

            # 先把根节点建立出来（前序遍历的第一个节点就是根节点）
            root = TreeNode(preorder[preorder_root])

            # 左子树的节点个数（根节点在后续遍历中的index - 后续遍历的起始位置）
            size_left_subtree = inorder_root - inorder_left

            # 右子树的节点个数
            print(preorder_left + 1,)  # +1是为了隔掉root
            print(preorder_left + size_left_subtree,)  # 左子树的终止位置
            print(inorder_left,)
            print(inorder_root - 1)

            print(">>>>>>>>>>>>>>>")

            print(preorder_left + size_left_subtree + 1,)
            print(preorder_right,)
            print(inorder_root + 1,)
            print(inorder_right)


            # 构建左子树
            root.left = mybuild(preorder_left + 1,  # +1是为了隔掉root
                                preorder_left + size_left_subtree,  # 左子树的终止位置
                                inorder_left,
                                inorder_root - 1)

            # 构建右子树
            root.right = mybuild(preorder_left + size_left_subtree + 1,
                                 preorder_right,
                                 inorder_root + 1,
                                 inorder_right)
            return root
        n = len(preorder)
        # 构造哈希映射，快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}  # 把中序遍历序列映射成一个字典方便递归函数查找
        return mybuild(0, n-1, 0, n-1)



s = Solution()

pre = [1,2,3]
ino = [2,3,1]
tree1 = s.buildTree1(pre, ino)





# print(tree.left.left)
print(">>>>>>>")