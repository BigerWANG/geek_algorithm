# coding: utf8


# 冒泡

def bubble_sort(l):
    """
    冒泡排序只会操作相邻的两个数据，
    每次冒泡都会对相邻的像个元素进行比较，看是否满足大小关系要求，
    如果不满足就让这两个元素互换，一次冒泡至少会让一个元素移动到他应该在的位置，重复n次，就完成了n个数据的排序
    时间复杂度是O(n**2)
    :return:
    个人理解：先循环一遍(for)，循环的同时还要去做比较(for)，每次循环都要将其中的一个元素与它的相邻的元素作比较，同时做交换
    """

    if len(l) <= 0:
        return "error"
    for i in range(len(l)):
        flag = False
        print "range: ", len(l) - 1 - i
        print "range: ", range(0, len(l) - 1 - i)
        for j in range(0, len(l) - 1 - i):  # 为了防止超出List范围， 之所以要 -1 是因为下边要+1: l[j] > l[j+1]
            if l[j] > l[j+1]:  # 如果后一个大于前一个，两者交换
                l[j], l[j+1] = l[j+1], l[j]
                flag = True
            print ">>>>l: ", l
        if not flag:
            break
    return l


# 插入排序
def insertion_sort(l):
    """
    插入排序
    将数组中的数据分为两个区间，已排序区间和未排序区间，初始已排序区间只有一个元素，就是数组的第一个元素，插入算法的核心思想是
    取未排序区间中的元素，在已排序区间中找到合适的位置将其插入，并保重已排序区间数据一直有序，重复这个过程，知道未排序区间中元素为空，算法结束
    时间复杂度n2
    :param l:
    :return:
    """

    if len(l) <= 0:
        return "error"

    for i in range(len(l)):
        value = l[i]  # 第一个元素
        for j in range(len(l[:i]), 0, -1):
            print j
            if l[j] > value:
                print l[j], l[j+1]
                l[j+1] = l[j]
            else:
                break
    return l


# 归并排序
def merge_sort(a):
    """
    1，分治法：分而治之，将大问题划分成若干个子问题
    2，递归：
    先把数组从中间分成两个部分，然后对前后两个部分分别排序，再将排好序的两部分分别合并在一起
    递归公式：merge_sort(p...r) = merge(merge_sort(p...q), merge_sort(q+1...r))
    递归终止条件: p >= r
    算法过程：
    1 先把待排序数组a 分为两个部分 q = len(a) / 2, left = a[q:], right = a[:q]
    2 将分开的两个数组使用排序函数merge：
      1）新建一个tmp数组用来存放已经排好序的数据， 和两个下标 i和j 分别指向left的第一个元素和right的第一个元素
      2）对比两个数组中的元素，两两对比，将最小的数放入tmp中， 并且对当前列表的下标+1
    3，重复1和2的步骤
    :return:
    """
    if len(a) <= 1:  # 设置边界条件
        return a
    q = len(a) / 2  # 找出中间节点
    left = merge_sort(a[:q])  # 以中间节点为分割点分别递归的对前一个和后一个进行排序
    right = merge_sort(a[q:])
    return _merge(left, right)  # 最后使用合并函数把排好序的两个list进行合并


def _merge(left, right):
    res = []  # 先声明一个空数组，用来存放对比过后的数据
    i = 0
    j = 0
    while i < len(left) and j < len(right):  # i和j两个index依次在left和right上取元素进行比较
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


# 快速排序
class QuickSorted(object):
    def sorted(self, array, l, r):
        if l < r:
            q = self.praition(array, l, r)
            self.sorted(array, l, q - 1)
            self.sorted(array, q+1, r)


    @staticmethod
    def praition(array, l, r):
        """
        获取位置下标
        :param array:
        :param l:
        :param r:
        :return:
        """
        x = array[r]
        i = l-1
        for j in range(l, r):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[r] = array[r], array[i+1]
        return i+1


def quick_sorted(L):
    return QuickSorted().sorted(L, 0, len(L) - 1)


def quick_sorted1(array):
    """
    最简单的快排写法
    """
    if not array or len(array) < 2:
        return array
    pivot = array[0]  # 选一个分界点
    less_than_p = [i for i in array if i <= pivot]
    bigger_than_p = [i for i in array if i > pivot]
    return quick_sorted1(less_than_p) + [pivot, ] + quick_sorted1(bigger_than_p)








def queryK(array, k):
    """
    :param array:
    :return:
    """
    if not array:
        return
    p = array[-1]
    for a in array:
        if a > p:
            pass


def bucket_sort():
    """
    :return:
    """
    pass


# 计数排序


if __name__ == '__main__':
    import random
    l = range(11)
    random.shuffle(l)
    print l
    quick_sorted(l)
    print l
