# coding: utf-8

"""
0-1背包问题
回溯法解决

我们有一个背包，背包总的承载重量是 Wkg。
现在我们有 n 个物品，每个物品的重量不等，并且不可分割。
我们现在期望选择几件物品，装载到背包中。
在不超过背包所能装载重量的前提下，如何让背包中物品的总重量最大？

"""

import sys


maxval = sys.maxsize

def package(i, cw, items, n, w, res):
    """

    :param i: 考察到哪个物品了
    :param cw: 已经装进去的物品的重量和
    :param items: 每个物品的重量，
    :param n: 物品个数
    :param w: 背包的承重
    :return:

    假设背包可承受重量为100kg, 物品个数是10，物品重量存储在数组a中，函数调为：
    package(0, 0, a, 10, 100)
    """
    global maxval
    if cw == w or i == n:
        if cw > maxval:
            maxval = cw
        print(items[i])
        return
    package(i + 1, cw, items, n, w, res) # 如果不装进背包的
    if cw + items[i] <= w:  # 装进背包
        # print(cw + items[i])
        # res.append(items[i])  # 把能装进去的物品翻到结果数组里
        package(i+1, cw + items[i], items, n, w, res)


def test():
    import random
    w = 100
    a = list(range(10, 30))
    random.shuffle(a)
    res = []
    package(0, 0, a, len(a), w, res)
    # print(res)
    # print(sum(res))
    print(maxval)

if __name__ == '__main__':
    test()
