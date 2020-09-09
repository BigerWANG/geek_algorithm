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


def BFS(graph, s):  # graph图  s指的是开始结点
    # 需要一个队列
    queue = []
    seen = set()  # 看是否访问过该结点
    queue.append(s)
    seen.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)  # 保存第一结点，并弹出，方便把他下面的子节点接入
        nodes = graph[vertex]  # 子节点的数组
        for w in nodes:
            if w not in seen:  # 判断是否访问过，使用一个数组
                queue.append(w)
                seen.add(w)
        print(vertex)



BFS(graph, "F")

