# coding: utf-8

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1:

输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
示例 2:

输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。


"""
from collections import deque


class Solution:
    def numIslands(self, grid):
        """
        广度优先遍历
        :param grid:
        :return:
        """
        nr = len(grid)  # 竖着的长度
        if nr == 0:
            return 0
        nc = len(grid[0]) # 横着的长度
        num_island = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_island += 1
                    grid[r][c] = "0"  # 把已经等于1 的元素转变成0，防止重复遍历
                    neighbors = deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        # 查看四周有没有陆地
                        around = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                        print(around)
                        for x, y in around:
                            # 确定 顶点是否在二维数组的范围里并且等于1
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"
        return num_island


def test():
    a = [["1"],
         ["1"]]
    s = Solution().numIslands(a)
    print(s)


if __name__ == '__main__':
    test()



