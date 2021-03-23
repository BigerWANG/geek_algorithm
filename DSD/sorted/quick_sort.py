# coding: utf-8
import random

def quick_sort(arr):
    if not arr or len(arr) < 2:
        return arr
    left = 0
    right = len(arr) - 1
    return _quick_sort(arr, left, right)


def _quick_sort(arr, left, right):
    if left < right:
        p = parition(arr, left, right)
        _quick_sort(arr, left, p-1)
        _quick_sort(arr, p+1, right)


def parition(arr, left, right):
    """原地排序"""
    # 选一个划分值
    x = arr[right]
    # 设定一个游标，把arr分成两部分，
    # arr[left ... i-1]的元素都是小于x的
    # arr[i ... right-1]的元素都是大于x的
    i = left
    for j in range(left, right):
        # 如果当前数字小于划分值
        if arr[j] < x:
            # 交换位置, 把当前数字和起始位置的数字交换
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # 这一步是干啥....
    arr[i], arr[right] = arr[right], arr[i]
    return i


if __name__ == '__main__':
    arr = [i for i in range(10)]
    random.shuffle(arr)
    print(arr)
    quick_sort(arr)
    print(arr)