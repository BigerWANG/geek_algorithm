# coding: utf-8
"""
406. 根据身高重建队列

假设有打乱顺序的一群人站成一个队列。
每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
编写一个算法来重建这个队列。

注意:
总人数少于1100人。

示例
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

第一遍：
[[7,0], [7,1], [5,2], [5,0], [6,1], [4, 4]]



[ [4,4], ]


[70, 71, 61, 50, 52, 44]


输出:
[[7,0], [5,0], [5,2], [6,1], [4,4], [7,1]]
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]

        算法：
        1，取最后一个人和前边的人比较，把符合条件的放到新队列里

        不会写！！！！
        """
        if not people:
            return []

        start = 0
        end = len(people) - 1
        res = [None] * len(people)

        while start <= end:
            e = people[end]
            count = 0
            while start <= end - 1:
                s = people[start]



        return res


p = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructQueue(p))





