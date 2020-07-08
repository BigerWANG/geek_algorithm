# coding: utf8

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = list()
        for inner in matrix:
            for i in inner:
                res.append(i)

        return res

def test():
    l = [[1,2,3], [4,5,6], [7,8,9]]
    print Solution().spiralOrder(l)

if __name__ == '__main__':
    test()