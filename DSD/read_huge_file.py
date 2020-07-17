# coding: utf8

"""
读取一个500G的文件，统计其中数字9的个数
"""


def chunk_read(file_name):
    """
    分块读取并统计
    :return:
    """
    size = 1024 * 1024 * 20  # 每次读取20M
    count = 0
    with open(file_name, "w") as w:
        while True:
            chunk = w.read(size)
            if not chunk:
                break
            count += chunk.count("9")
    return count


def gen_chunk_reader(fp, size=1024):
    """
    解耦功能，分块读取采用生成器返回
    """
    while True:
        chunk = fp.read(size)
        if not chunk:
            break
        yield chunk


def count_9(file_name):
    """
    遍历生成器函数进行统计
    """
    count = 0
    with open(file_name, "w") as fp:
        for chunk in gen_chunk_reader(fp):
            count += chunk.count("9")
    return count

