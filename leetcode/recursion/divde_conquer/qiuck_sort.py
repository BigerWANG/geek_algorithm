# coding: utf-8

"""
快速排序
先找出一个中间点

"""

class QuickSorted:
    def __sorted(self, array, l, r):
        if l < r:  # 递归终止条件
            q = self.__praition(array, l, r)  # 对数组进行划分
            self.__sorted(array, l, q -1)  # 左边的数组
            self.__sorted(array, q+1, r)  # 右边的数组

    @staticmethod
    def __praition(array, l, r):
        x = array[r]  # 传入数组的最后一个值
        i = l-1
        for j in range(l, r):
            if array[j] < x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[r] = array[r], array[i+1]
        return i+1

    def quick_sorted(self, array):
        self.__sorted(array, 0, len(array) - 1)


res = [1,2,2,1,3,1]
QuickSorted().quick_sorted(res)
print(res)
