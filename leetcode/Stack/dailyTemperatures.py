# coding: utf-8

"""
请根据每日 气温 列表，重新生成一个列表。
对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。
每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        维护一个递减栈（单调栈）保存队列的index，后入栈的元素总比栈顶元素小
        """
        # 声明一个栈
        stack = []
        # 生成一个和T长度相等的数组，用于保存结果
        res_list = [0] * len(T)

        for index, val in enumerate(T):
        	# 如果栈顶元素的值小于当前值，说明找到了大于当前值的温度
        	while stack and T[stack[-1]] < val:
        		# 按索引插入结果数组，结果是当前的索引值 - 栈顶的值
        		res_list[stack[-1]] = index - stack[-1]
        		stack.pop()
        	stack.append(index)
        return res_list



        
def test():
	t = [73, 74, 75, 71, 69, 72, 76, 73]
	print Solution().dailyTemperatures(t)

if __name__ == '__main__':
	test()
        	

