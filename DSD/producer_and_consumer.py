# coding: utf-8
import threading
import time
from Queue import Queue
# 生产者-消费者模式


class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print("start put task ", i)
            self.data.put(i)
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print("I got task ", val)


def main():
    q = Queue()
    p = Producer("Producer", q)
    c = Consumer("Consumer", q)
    p.start()
    c.start()
    p.join()
    c.join()
    print("all task is done")


def main1():
    q = Queue()
    q.put("x")

if __name__ == '__main__':
    main()

