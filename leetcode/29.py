# coding: utf-8


"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [ [1,2,3],
                [4,5,6],
                [7,8,9]]

输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [ [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


"""


class Solution(object):

    def spiralOrder0(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        res = []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])  # 从左到右
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                res.append(matrix[i][r])  # 从上到下
            r -= 1
            if l > r:
                break

            for i in range(r, l -1, -1):
                res.append(matrix[b][i])  # 从左到右
            b -= 1
            if t > b:
                break
            for i in range(b, t -1 , -1):
                res.append(matrix[i][l])  # 从下到上
            l += 1

            if l > r:
                break
        return res




    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]

        return res




def test():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    # print Solution().spiralOrder1(matrix)
    print Solution().spiralOrder0(matrix)


if __name__ == '__main__':
    test()
