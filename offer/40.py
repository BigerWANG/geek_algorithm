# coding: utf-8

"""
最小的 K 个数

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
"""


class Solution(object):
    @staticmethod
    def get_least_numbers_heap(arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        加入到heap中，从堆顶依次取出K个值
        """
        if not arr:
            return []
        import heapq
        return heapq.nsmallest(k, arr)

    @staticmethod
    def get_least_numbers_sort(arr, k):
        """
        用快排先排序arr, 再取出来前K个数
        """
        if not arr:
            return []

        def __sroted(arr):
            p = arr[0]
            left_arr = [i for i in arr if i < p]
            right_arr = [i for i in arr if i >= p]
            return left_arr + [p, ] + right_arr
        sk = __sroted(arr)
        return sk[:k]


def test():
    pass


if __name__ == '__main__':
    test()
