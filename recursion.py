# coding: utf-8


def find_recommender(recommender):
    """
    寻找最终推荐人
    :return:
    find(n) 的功能就是找n 的下一个人，直到n的下一个人是空，返回n
    1，递推公式：find(n) = find(n)
    2，终止条件 find(n) == None
    """

    print "....select recommender: %s" % recommender  # 此处写查询逻辑
    final_recommender = ""
    if not find_recommender(final_recommender):
        return final_recommender


def step(n):
    """
    假如有n个台阶，每次你可以跨1个台阶或2个台阶，请问走这n个台阶有多少种走法
    1, 递推公式：f(n) = f(n-1) + f(n-2)  # f(n-1) 是每次走一个台阶，f(n-2)是每次走两个台阶
    2, 终止条件 f(2) = 2， f(1) = 1
    :param n:
    :return:
    """
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    return step(n-1) + step(n-2)


def deduplication_step(n):
    """
    去重版 使用哈希表保存递归数据，去除重复计算
    :param n:
    :return:
    """
    hash_table = dict()
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    if hash_table.get(n):
        return hash_table[n]
    ret = step(n-1) + step(n-2)
    hash_table[n] = ret
    return ret


# ############################  面试题

def cell_division(n):
    """
    细胞分裂 有一个细胞 每一个小时分裂一次，一次分裂一个子细胞，第三个小时后会死亡。那么n个小时候有多少细胞
    1, 递推公式：f(n) = f
    2, 终止条件 n % 3 == 0 return
    :return:
    """




if __name__ == '__main__':
    print deduplication_step(12)
