# coding: utf8

"""
无向图 邻接链式存储
维护一个节点为链表的数组
数组存储图的顶点
链表连接定点的相关顶点
"""
from collections import defaultdict


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
            print(current_node.val)
            node_list.append(current_node)
            current_node = current_node.next_node
        return node_list



class DictGraph(object):
    def __init__(self):
        """邻接表存储，字典key顶点，每个顶点都对应一个set"""
        self.graph = defaultdict(list)  # 也可以使用set去重
        self.step = 0


    def add_point(self, s, t):
        """
        :param int s:
        :param int t:
        :return:
        """
        self.graph[s].append(t)  # 无向图存储两遍
        self.graph[t].append(s)

    def BFS(self, s, t):
        """
        广度优先搜索
        :param int s: 开始顶点
        :param int t: 目标顶点
        """
        self.step = 0
        if not s in self.graph.keys():
            return
        queue = []  # 保存图中的顶点
        visited = set()  # 去重
        queue.append(s)  # 起始点
        visited.add(s)
        while queue:
            vertex = queue.pop(0)
            for i in self.graph[vertex]:
                if i == t:
                    print("found it! cost %d step" % self.step)
                    return
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
                    self.step += 1
            # print(vertex)

    def DFS(self, s, t):
        """
        深度优先
        :param int s: 开始顶点
        :param int t: 目标顶点
        :return:
        """
        self.step = 0
        # queue本质上是堆栈，用来存放需要进行遍历的数据
        # order里面存放的是具体的访问路径
        queue, order = [], []
        # 首先将初始遍历的节点放到queue中，表示将要从这个点开始遍历
        queue.append(s)
        while queue:
            # 从queue中pop出点v，然后从v点开始遍历了，所以可以将这个点pop出，然后将其放入order中
            # 这里才是最有用的地方，pop（）表示弹出栈顶，由于下面的for循环不断的访问子节点，并将子节点压入堆栈，
            # 也就保证了每次的栈顶弹出的顺序是下面的节点
            v = queue.pop(0)
            order.append(v)
            # 这里开始遍历v的子节点
            for w in self.graph[v]:
                if w == t:
                    print("found it! cost %d step" % self.step)
                    return
                # w既不属于queue也不属于order，意味着这个点没被访问过，所以讲起放到queue中，然后后续进行访问
                if w not in order and w not in queue:
                    queue.append(w)
                    self.step += 1
        return order


    def RECUR_DFS(self, s, t):
        """
        深度优先
        :param int s: 开始顶点
        :param int t: 目标顶点
        :return:
        """
        visited = set()
        return self.recur_dfs(s, t, visited)

    def recur_dfs(self, vertex, t, visited):
        """
        :param int w:
        :param int t:
        :param set visited:
        :return:
        """
        self.step += 1
        if t in visited:
            return
        print(">>>>")
        print(visited)
        print(vertex)
        print(">>>>\n")
        if vertex == t:
            print("found it! cost %d step" % self.step)
            return
        visited.add(vertex)
        for i in self.graph[vertex]:
            if i not in visited:
                self.recur_dfs(i, t, visited)







g = DictGraph()
g.add_point(0, 1)
g.add_point(0, 3)

g.add_point(1, 2)
g.add_point(1, 4)

g.add_point(2, 5)

g.add_point(3, 4)

g.add_point(4, 5)
g.add_point(4, 6)

g.add_point(5, 7)

g.add_point(6, 7)

import json

print(json.dumps(g.graph, indent=4))

g.RECUR_DFS(0, 5)
# g.BFS(0, 5)
# ----------------------BFS------------------------


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}


