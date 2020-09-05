# coding: utf-8
"""
递归的代码模板

def recursion(level, param1, param2):
    # 递归终止条件
    if level > MAX_LEVEL or not level: # 大于、小于某个终止条件
        process_result
	   return
    # 处理当前层逻辑
    process(level, data...)
    # 下探到下一层
    self.recursion(level + 1, p1, ...)
    # 清理当前层


思维要点：
1，不要人肉递归
2，找到最近最简方法，将其拆解成可重复解决的子问题(重复子问题)
3，数学归纳法的思维
"""


def c(n):
    # 先判断终止条件
    if n < 1:
        return 1
    # 进行每层的处理
    return n * c(n-1)


class Solution(object):
    """22.生成有效的括号"""
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        self.res = []
        self.generate(0, 0, n, "")
        return self.res

    def generate(self, left, right, n, s):
        # 终止条件
        if left == n and right == n:
            self.res.append(s)

        # 处理当前层
        if left < n:
            self.generate(left + 1, right, n, s + "(")
        if left > right:
            self.generate(left, right + 1, n, s + ")")
            # 下探到下一层
            # 清理当前层



print Solution().generateParenthesis(3)