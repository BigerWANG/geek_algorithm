# coding: utf-8

"""

将有序数组转换成高度平衡的二叉搜索树

一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。


给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        二分法生成BST，
        先取中间节点，
        中间节点左边的元素是左子树
        中间节点右边的元素是右子树
        递归重复这个过程
        """
        if not nums: return
        def helper(left, right):
            if left > right:
                return
            mid = (left + right) / 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) -1)




def binary_search(nums, target):
    if not nums: return
    start = 0
    end = len(nums) -1
    step = 0
    while start < end:
        mid = (start + end) // 2
        step += 1
        if nums[mid] > target:  # 如果中间节点 > target, 那么以中间节点为结束点
            end = mid
        elif nums[mid] < target: # 如果中间节点 < target，那么以中间节点为开始节点
            start = mid
        else:
            break
    return step

def curs_binary_search(nums, target):
    if not nums: return
    def helper(start, end, step):
        if start > end:
            return
        mid = (start + end) // 2
        step += 1
        if nums[mid] > target:  # 如果中间节点 > target, 那么以中间节点为结束点
            helper(start, mid, step)
        elif nums[mid] < target: # 如果中间节点 < target，那么以中间节点为开始节点
            helper(mid, end, step)
        else:
            print("找到了", nums[mid], "花费了{}步".format(step))
            return

    return helper(0, len(nums) - 1, 0)


def test():
    # print(binary_search(range(100), 53))
    curs_binary_search(range(100), 53)





if __name__ == '__main__':
    test()




