# coding: utf-8

"""
根据array生产二叉树
"""

from collections import deque, defaultdict
class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.list = []

    def __repr__(self):
    	return "<Node {}>".format(self.data)



    def preorder(self):
    	if self.data is not None:
           	self.list.append(self.data)
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
        return self.data

    def inorder(self):
    	if self.left is not None:
            self.left.inorder()
    	if self.data is not None:
            print self.data
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
			d.append(head.left) # 左子节点入队
			head.right = TreeNode(next(iter_value)) # 再下一个就是又子节点
			d.append(head.right)  # 右子节点入队
		except StopIteration as e:  # 直到生成器为空，取不出来下一个节点为止
			break

	return root
		

def pre_traverse_tree(root):
	if not root:
		return 
	print pre_traverse_tree(root)
	print pre_traverse_tree(root.left)
	print pre_traverse_tree(root.right)
	# return root.data
	
	
def levelOrder(root):
	"""
	层序遍历 二叉树
	"""
	d = defaultdict(list)
	def f(r, i):
	    if r:
	        d[i].append(r.data)
	        f(r.left, i+1)
	        f(r.right, i+1)
	f(root, 0)
	return [i for i in d.values()]

def level_bfs(tree):

	"""
	层序遍历，返回二维数组
	"""
	res = []
	q = deque()
	q.append(tree)
	while q:
		level = []
		for _ in range(len(q)):  # 在每一层开始遍历前，先记录这一层的节点数量，然后一口气处理完这一层的n个节点
			node = q.popleft()	
			level.append(node.data)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		res.append(level)
	return res

def bfs(tree):
	"""
	层序遍历 返回一位数组
	"""
	res = []
	q = deque()
	q.append(tree)
	while q:
		print q
		node = q.popleft()
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
	return res
        
if __name__ == '__main__':
	arr = [3,9,20,None,None,15,7]
	t = gen_tree(arr)

	q1 = level_bfs(t)
	q2 = bfs(t)
	print q1
	print q2

	# tree.preorder()
	# tree.inorder()






