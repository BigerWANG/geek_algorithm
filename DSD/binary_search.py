# coding: utf-8

"""
二分查找的四种变形
"""




def search_first_item(array, target):
    """
    查找第一个匹配的元素
    :return:
    """
    if not array:
        return -1

    start, end = 0, len(array) - 1


    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid
        elif array[mid] < target:
            start = mid
        else:  # 这个时候需要看mid是不是第一个与target相等的元素
            if mid == 0 or array[mid - 1] != target:
                return mid
            else:
                end = mid
    return -1





def search_last_item(array, target):
    """
    查找最后一个匹配的元素
    :return:
    """
    if not array:
        return -1

    start, end = 0, len(array) - 1


    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid
        elif array[mid] < target:
            start = mid
        else:  # 这个时候需要看mid是不是最后一个与target相等的元素
            if array[mid + 1] != target:
                # mid+1 != target说明 下一个元素也不等于，
                return mid
            else:
                start = mid
    return -1




if __name__ == '__main__':
    a = [1,3,4,5,6,8,8,8,11,18]
    t = 8
    print(search_first_item(a, t))
    print(search_last_item(a, t))



