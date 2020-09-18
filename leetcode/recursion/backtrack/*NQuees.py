# coding: utf-8

"""
51. N 皇后

N*N的棋盘，需要放置N个皇后，要求不能互相攻击
皇后会攻击一行，一列，和对角线上的其他棋子


算法：
1， 为了判断一个位置所在的列和两条斜线上是否已经有皇后，使用三个集合 columns，diagonals1 和 digonals2
分别记录每一列以及两个方向的每条斜线上是否有皇后

2，列的表示法很直观，一共有N列，每一列的下标范围从0到N-1,使用列的下标即可明确表示每一列

3，对于每个方向上的斜线，需要找到斜线上的每个位置的行下标与列下边之间的关系

4，方向一同一条斜线上的每个位置满足行下标与列下标之差相等： (0,0) 与(2,2)在同一条斜线上 （0，4）（1，5）
   方向二的同一条斜线上的每个位置满足行下标与列下标之和相等：
"""



class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def generate_board():
            """生成棋盘函数"""
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board


        def backtrack(row):
            """回溯函数"""
            if row == n:
                board = generate_board()
                solutions.append(board)
                return

            for i in range(n):
                # 这一步是判断当前位置i是否在不能放置的位置上
                if i in columns or row -i in diagonal1 or row +i in diagonal2:
                    continue
                queens[row] = i     # 这个i就是放置皇后的位置

                columns.add(i)            # 把这个位置添加到不同的
                diagonal1.add(row-i)
                diagonal2.add(row+i)

                backtrack(row + 1)

                columns.remove(i)         # 回溯
                diagonal1.remove(row - i)
                diagonal2.remove(row + i)

        solutions = []
        queens = [None] * n
        columns = set()    # 保存相同位置的列
        diagonal1 = set()  # 保存相同位置的左斜线
        diagonal2 = set()  # 保存相同位置的右斜线
        row = ["."] * n
        backtrack(0)
        return solutions

