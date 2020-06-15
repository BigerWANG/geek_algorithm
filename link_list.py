# coding: utf8


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
1, 单链表反转
2, 链表中环的检测
3, 两个有序的链表合并
4, 删除链表倒数第 n 个结点
5, 求链表的中间结点
"""


def is_palindrome(head):
    """
    判断一个单链表是否回文

    :param self:
    :param node:
    :return:
    解法：
    1.设置快慢指针slow，fast， 从head开始
    2，慢指针向前一步，快指针向前两步
    3，快指针的next为null时，慢指针正好走到中间
    4，慢指针slow继续向前，同时反转后半部分的链表，将next设置成prev,将prev设置成slow,将slow设置成next
       prev , slow, slow.next = slow, slow.next, slow.prev
    5,一个从头开始，一个从中间开始，依次比较，如果都相等就返回True
    """

    slow, fast, prev = head, head, None
    while fast is not None:
        slow = slow.next
        fast = fast.next.next if fast.next else fast.next
    while slow is not None:
        slow.next, slow, prev = prev, slow.next, slow

    while head and prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next

    return True


def merge_two_list(l1, l2):
    """
    合并两个有序链表：归并的思想
    将两个有序链表合并成一个新的有序链表并返回
    1，先初始化一个空数组
    2，设置两个指针分别指向l1,l2的头部
    3,每次从l1 和l2取出数据进行比较
    4，较大的那个数放入空数组, 对应的指针+1
    5，直到一方为空，停止比较，将另一方剩下的数添加进数组(如果存在)
    """



def two_sum(nums, target):
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

    :param nums:
    :param target:
    :return:
    解法：
    两遍哈希表：
    第一遍循环将nums的元素对应index保存到dict中
    再次遍历nums, 判断target-i 是否在dict中，如果在 返回对应的index
    """
    hash_map = dict()
    for index, val in enumerate(nums):
        if (target - val) in hash_map.keys():
            return [index, hash_map[target - val]]
        hash_map[val] = index


def removeDuplicates(nums):
    """
    删除有序数组中的重复项，空间复杂度为O(1)

    """
    pass


if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [3, 4, 5]
