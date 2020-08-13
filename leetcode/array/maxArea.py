# coding: utf-8

"""
盛水最多的容器
https://leetcode-cn.com/problems/container-with-most-water/
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        双指针，
        一个指向头一个指向尾
        每次让比较小的那个移动，并记录下来移动后的容积
        """

        start, end = 0, len(height) - 1
        ans = 0  # 设置一个哨兵变量，可以保存最大值
        while start < end:
            h = min(height[start], height[end])  # 算出来高度，比较小的是容器的高度
            ans = max(ans, h * (end - start))  # end - start是算出来容器的宽度
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return ans

if __name__ == '__main__':
    p = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(p))

