# coding: utf-8

"""
面试题 01.08. 零矩阵

编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        先把0的坐标记录下来 row AND col
        再循环row和col去清零行和列
        """
        if not matrix:
            return []

        row, col = set(), set()
        h, w = len(matrix), len(matrix[0])  # 高度和宽度

        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in row:
            for j in range(w):
                matrix[i][j] = 0

        for i in range(h):
            for j in col:
                matrix[i][j] = 0









def test():
    matrix = \
        [
            [1,1,1],
            [1,0,1],
            [0,1,1]
        ]
    Solution().setZeroes(matrix)
    for i in matrix:
        print i

if __name__ == '__main__':
    test()
