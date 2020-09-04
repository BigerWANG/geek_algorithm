# coding: utf-8


"""
881. 救生艇

第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
 

示例 1：

输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
示例 2：

输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)
示例 3：

输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)
提示：

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000

"""


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        算法
        先把数组排序
        令 people[i] 指向当前最轻的人，而 people[j] 指向最重的那位。
        然后，如上所述，如果最重的人可以与最轻的人共用一条船（即 people[j] + people[i] <= limit），那么就这样做；否则，最重的人自己独自坐在船上。
        """
        if not people:
            return -1

        res = 0
        people.sort()
        start = 0
        end = len(people) - 1

        while start <= end:
            s = people[start]
            e = people[end]
            if (s + e) <= limit:
                # 如果最轻的人和最重的人都可以坐的下
                start += 1
            end -= 1  # 最重的人独自坐在船上--
            res += 1
        return res


    def numRescueBoats1(self, people, limit):
        """错误的结果"""
        if not people:
            return -1
        res = 0
        for p in people:
            max_p = max(people[people.index(p)+1:])
            if p + max_p <= limit and people.index(p) != people.index(max_p):
                people.remove(p)
                people.remove(max_p)
                res += 1
            else:
                people.remove(max_p)
                res += 1
        return res
people = [3,2,2,1]
limit = 3

print(Solution().numRescueBoats(people, limit))