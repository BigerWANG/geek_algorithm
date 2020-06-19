# coding: utf-8


"""
two stack to a queue
"""


class CQueue(object):

    def __init__(self):
        self.__append_stack = []
        self.__delete_stack = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.__append_stack.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.__delete_stack:
            return self.__delete_stack.pop()

        if not self.__append_stack:
            return -1

        else:
            while self.__append_stack:
                self.__delete_stack.append(self.__append_stack.pop())
            return self.__delete_stack.pop()





def test():
    q = CQueue()
    q.appendTail(1)
    q.appendTail(2)
    q.appendTail(3)
    q.appendTail(4)



    print q.deleteHead()
    print q.deleteHead()
    print q.deleteHead()
    print q.deleteHead()
    print q.deleteHead()


if __name__ == '__main__':
    test()
