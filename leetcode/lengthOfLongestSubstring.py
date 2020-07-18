# coding: utf-8

"""
最长不重复子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        滑动窗口的思想
        维护一个队列，按下表往队列里添加字符串，并且查看这个窗口里有没有重复的值，有的话就出队
        查看有没有重复值的方法是设置一个set
        """
        if not s:
            return
        left = 0  # 左侧的index
        lookup = set()  # 设置一个set保存重复元素
        n = len(s)
        max_len, curr_len = 0, 0
        for i in range(n):
            curr_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])  # 如果当前元素在set中，移除set中的当前元素
                left += 1
                curr_len -= 1
            if curr_len > max_len:
                max_len = curr_len
            lookup.add(s[i])
        return max_len

