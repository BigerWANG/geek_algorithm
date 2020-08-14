# coding: utf-8

"""
下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""


class Solution(object):
    def nextPermutation(self, height):
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
    print(Solution().nextPermutation(p))

