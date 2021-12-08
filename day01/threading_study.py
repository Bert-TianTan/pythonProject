import threading
import time
import json

exitFlag = False

threadLock = threading.Lock()
threads = []


class FirstThread(threading.Thread):
    def __init__(self, _threadId, _name, _counter):
        threading.Thread.__init__(self)
        self.threadID = _threadId
        self.name = _name
        self.counter = _counter

    def run(self) -> None:
        print("start thread....%s\n" % self.name)
        # 获取锁 用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        # 释放锁 开启下一个线程
        threadLock.release()
        print("exit thread....%s" % self.name)


def print_time(thread_name, delays, counters):
    while counters:
        if exitFlag:
            thread_name.exit()
        time.sleep(delays)
        print("%s: %s\n" % (thread_name, time.ctime(time.time())))
        counters -= 1




