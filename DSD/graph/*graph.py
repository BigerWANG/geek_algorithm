# coding: utf8

"""
无向图 邻接链式存储
维护一个节点为链表的数组
数组存储图的顶点
链表连接定点的相关顶点
"""


class LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next_node = None


class LinkedList(object):
    """单链表"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.next_node = None

    def add_node(self, item):
        """从尾部添加节点"""

        if not isinstance(item, LinkedListNode):
            item = LinkedListNode(item)

        if not self.head:
            self.head = item
        else:
            self.tail.next_node = item
        self.tail = item

    def output_list(self):
        """输出单链表"""

        current_node = self.head
        node_list = []
        while current_node is not None:
            print current_node.val
            node_list.append(current_node)
            current_node = current_node.next_node
        return node_list


class Graph(object):
    def __init__(self, length):
        """数组存储顶点，每个顶点都是链表的头结点"""
        self.length = length
        self.graph_list = [LinkedList() for _ in range(length)]

    def add_point(self, s, t):
        """
        :param int s:
        :param int t:
        :return:
        """
        s_node = LinkedListNode(s)
        t_node = LinkedListNode(t)

        self.graph_list[s].add_node(t_node)  # 无向图存储两遍
        self.graph_list[t].add_node(s_node)

    def BFS(self, s):
        """
        广度优先搜索
        """

        queue = []
        visited = set()
        node = self.graph_list[s[0]].output_list()[s[1]]
        queue.append(node)
        visited.add(self.graph_list[s])

        while queue:
            w = queue.pop(0)
            while w:
                w = w.next_node()
                if w not in visited:
                    queue.append(w)
                    visited.add(w)
            print w


g = Graph(8)
g.add_point(0, 1)
g.add_point(0, 3)

g.add_point(1, 2)
g.add_point(1, 4)

g.add_point(2, 1)
g.add_point(2, 5)

g.add_point(3, 4)

g.add_point(4, 5)
g.add_point(4, 6)

g.add_point(5, 2)
g.add_point(5, 7)

g.add_point(6, 7)

g.add_point(7, 5)

h = g.graph_list[0]
g.BFS((0, 0))
# ----------------------BFS------------------------


