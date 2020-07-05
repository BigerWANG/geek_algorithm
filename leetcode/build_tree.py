# coding: utf-8

"""
根据array生产二叉树
"""
class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.l = []

    def __repr__(self):
    	return "<Node {}>".format(self.data)

   	def preorder(self):
		if self.data is not None:
		    print self.data
		if self.left is not None:
		    self.left.preorder()
		if self.right is not None:
		    self.right.preorder()


    def inorder(self):
    	if self.left is not None:
            self.left.inorder()
    	if self.data is not None:
            print self.data
        if self.right is not None:
            self.right.inorder()
		

def create_btree_by_list(array):
	"""
	把数组按层遍历，生产二维数组
	"""

	def create_btree_one_step_up(btree_list, forward_level):
		new_btree_list = []
		i = 0
		for elem in forward_level:
			root = TreeNode(elem)
			if 2*i < len(btree_list):
				root.left = btree_list[2*i]
			if 2*i +1 < len(btree_list):
				root.right = btree_list[2*i + 1]
			new_btree_list.append(root)
			i += 1

		return new_btree_list

	i = 1
	level_order = []  # 先按层遍历，这里保存每一层的节点
	while True:
		s, e = i-1, 2*i-1  # 切片索引
		level_nodes = array[s: e]
		if not level_nodes:
			break
		level_order.append(level_nodes)
		i *= 2
	print "level_order>>>>", level_order
	# level_order = [i for i in level_order if i] 

	# print level_order  # 生成了按层序遍历的数结构


	if len(level_order) == 1:  # 如果只有一层，生成一个节点就ok
		return TreeNode(level_order[0][0])
	else:
		# 这里开始按层从下往上生成树
		btree_list = [TreeNode(elem) for elem in level_order[-1]]
		print btree_list

	for i in range(len(level_order)-2, -1, -1):
		btree_list = create_btree_one_step_up(btree_list, level_order[i])

	return btree_list[0]


	
if __name__ == '__main__':
	arr = [3,9,20,None,None,15,7]
	tree = create_btree_by_list(arr)
	print ">>>>.", tree.left.data
	tree.data
	def o(root):
		l = []
		if not root:
			return l
		l.append(o(root))
		l.append(o(root.left))
		l.append(o(root.right))
		return root.data
	print o(tree)

	# tree.inorder()






