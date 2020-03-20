#coding=utf-8
from multiprocessing import Process
import time

def pstart(arg):
    var = 0
    for i in range(100000000):
        var += 1

if __name__ == '__main__':
    p1 = Process(target = pstart, args = ("1", ))
    p2 = Process(target = pstart, args = ("2", ))
    start_time = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Two process cost time: %s" % (time.time() - start_time))
    start_time = time.time()
    pstart("0")
    print("Current process cost time: %s" % (time.time() - start_time))