# coding: utf-8

"""

面试题 01.07. 旋转矩阵
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？
 

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        使用原地交换
        """
        from copy import deepcopy
        l = len(matrix)
        new_matrix = deepcopy(matrix)  # 注意python中的赋值操作，二维数组中不能直接直接在原数组中交换
        for i in range(l):
            for j in range(l):
                new_matrix[i][j] = matrix[-(j + 1)][i]
        return new_matrix


def test():
    matrix = \
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    matrix = Solution().rotate(matrix)
    for i in matrix:
        print i

if __name__ == '__main__':
    test()
