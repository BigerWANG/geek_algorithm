# coding: utf-8

"""
divide sorted
归并排序
分治法
"""


def merge_sort(array):
    """
    1, 分治法，将大问题划分成若干子问题
    2，递归：
    """

    def _merge(left, right):
        """合并两个有序数组的逻辑"""
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[i]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

    if len(array) <=1:
        return array

    q = len(array) // 2 # 每次递归都找出中间节点
    left = merge_sort(array[:q])  # 分别对中间节点的左右子数组进行排序
    right = merge_sort(array[q:])
    return _merge(left, right)


res = merge_sort([5,4,3,2,1])
print(res)
