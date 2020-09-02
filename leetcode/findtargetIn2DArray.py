# coding: utf-8

"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。
"""



class Solution(object):
    def findtargetIn2DArray(self, matrix, target):
        """
        取右上角或者左下角作为参照点，
        以右上角为例
        比参照点大：往下移动一行
        比参照点小：往左移动列
        """

        row, cloum = 0, -1 # 取右上角
        while True:
            if target == matrix[row][cloum]:
                return True
            # 大于参照点，向下移动一行，row + 1
            elif target > matrix[row][cloum]:
                row += 1
            elif target < matrix[row][cloum]:
                cloum -= 1
            if row > len(matrix) - 1 or abs(cloum) == len(matrix):
                return False


s = Solution()


m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

t = 100

print(s.findtargetIn2DArray(m, t))


















