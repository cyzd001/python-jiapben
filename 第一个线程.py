import threading
import time


class myThread (threading.Thread):
    def __init__(self, threadid, name, counter):
        threading.Thread.__init__(self)
        self.threadid = threadid
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
print("******"+thread1.getName())  #返回线程名称
print(threading.currentThread())    #返回当前的线程变量
print(threading.enumerate())        #返回当前运行线程的list
print(threading.activeCount())      #返回正在运行的线程数量
# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)



# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
