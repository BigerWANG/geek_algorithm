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
        """
        if not s:
            return 0
        left = 0
        lookup = set()
        max_len, curr_len = 0, 0  # 最大长度和当前窗口长度
        for i in range(len(s)):
            curr_len += 1
            while s[i] in lookup:  # 如果有重复的，进入循环
                lookup.remove(s[left])
                left += 1  # 这里+1是移动窗口的位置
                curr_len -= 1  # 这里-1是表示移动后的窗口长度-1
            lookup.add(s[i])
            max_len = max(max_len, curr_len)
        print lookup
        return max_len


def test():
    s = "pwwkewwwwwwwww"
    print Solution().lengthOfLongestSubstring(s)


if __name__ == '__main__':
    test()

