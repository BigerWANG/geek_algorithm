# coding: utf-8

"""
买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        维护一个单调栈，栈顶是最大值，依次向下递减

        变量p
        如果栈顶大于p，pop掉栈顶
        如果栈顶小于p，p入栈
        最后结果是栈顶 - 栈底
        """
        s = []
        ret = 0
        if not prices:
            return 0
        for i in prices:
            while s and s[-1] >= i:
                top = s.pop()
                if not s:
                    continue
                ret = max(ret, top - s[0])
            s.append(i)
        return s[-1] - s[0] if s else 0

    def maxProfit1(self, prices):
        stack = []
        n = len(prices)
        for i in range(n):
            if not stack or prices[i] < prices[stack[-1]]:
                stack.append(i)
        maxPro = 0
        for i in range(n - 1, -1, -1):
            if i == stack[-1]:
                stack.pop()
                continue
            if prices[i] > prices[stack[-1]]:
                maxPro = max(maxPro, prices[i] - prices[stack[-1]])
        return maxPro

def test():
    s = Solution()
    print s.maxProfit1([7, 1, 5, 3, 6, 4])


if __name__ == '__main__':
    test()
