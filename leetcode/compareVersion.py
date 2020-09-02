# coding: utf-8

"""
比较版本号

比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。
 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。
你可以假设版本号的每一级的默认修订版号为 0。
例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
 

示例 1:

输入: version1 = "0.1", version2 = "1.1"
输出: -1
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if not version1 or not version2:
            return -1
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]

        n1, n2 = len(v1), len(v2)
        # 比较两个版本号，以长度较长的为准来比较
        for i in range(max(n1, n2)):
            i1 = int(v1[i]) if i < n1 else 0  # 如果超过长度就用0来替代
            i2 = int(v2[i]) if i < n2 else 0
            if i1 != i2:
                return -1 if i1 < i2 else 1
        return 0


def test():
    v1 = "01"
    v2 = "1"
    print(Solution().compareVersion(v1, v2))


if __name__ == '__main__':
    test()