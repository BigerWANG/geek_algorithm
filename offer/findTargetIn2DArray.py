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
        将二维数组压缩成一维数组
        """
        if not matrix or not target:
            return False
        heap = []
        for i in matrix:
            heap.extend(i)

        if target in heap:
            return True
        return False

    def leftFlagfindTargetIn2DArray(self, martix, target):
        """
        设置标志位：
        左下角：同一列的最大值，同一行的最小值

        将左下角设置为标志位：lflag: target > lflag, 跳过所在列；target < lflag，跳过所在行
        将右下角设置为标志位：rflag target > rflag
        """
        if not martix:
            return False
        h_index = 0  # 所在行index
        l_index = -1  # 所在列index
        while True:
            try:
                flag = martix[l_index][h_index]
                print flag
            except IndexError:  # 如果数组越界，返回
                return False
            if target > flag:  # 跳过flag所在列, h_index += 1
                h_index += 1
            if target < flag:  # 跳过flag所在行 l_index -= 1
                l_index -= 1
            if target == flag:
                return True

    def rightFlagfindTargetIn2DArray(self, martix, target):
        """
        设置标志位：
        右上角：同一列的最小值，同一行的最大值

        将右下角设置为标志位：rflag target > rflag
        """
        if not martix:
            return False
        h_index = 0  # 所在行index
        l_index = -1  # 所在列index
        while True:
            try:
                flag = martix[l_index][h_index]
            except IndexError:  # 如果数组越界，返回
                return False
            if target > flag:  # 跳过flag所在列, h_index += 1
                h_index += 1
            if target < flag:  # 跳过flag所在行 l_index -= 1
                l_index -= 1
            if target == flag:
                return True






def test():
    matrix = [
      [1,  4,  7, 11, 15],
      [2,  5,  8, 12, 19],
      [3,  6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    target = 5
    print(Solution().leftFlagfindTargetIn2DArray(matrix, target))


if __name__ == '__main__':
    test()
