import threading
import time
from .getInfo import getCardsInfo
from queue import Queue
import _thread
from .db_operate import update_db
import  demjson3

infoQueue= Queue(maxsize = 200)

class getInfoThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        for i in demjson3.decode(self.name):
            print ("开启线程："+ i)
        while(1):
            for i in demjson3.decode(self.name):
                infoQueue.put(getCardsInfo(i))
        for i in demjson3.decode(self.name):
            print ("退出线程：" + i)

def consumerThread():
    "开始启动线程"
    print("开始启动线程")
    def comsumer():
        while(1):
            if not infoQueue.empty():
                update_db(infoQueue.get())
    try:
        _thread.start_new_thread(comsumer())
    except Exception as e:
        print("错误信息consumerThread:{}".format(e))

# thread1 = getInfoThread(1,"边牧线程")
# thread1.start()
# thread1.join()
# print("退出线程")





# q= Queue(maxsize = 5)
# for i in range(5):
#     q.put(i)
# print(q.qsize())
# while(1):
#     if q.qsize() == 0:
#         break;
#     print("获得的信息:{},队列长度:{},队列是否满了:{},队列是否空了：{}".format(q.get(),q.qsize(),q.full(),q.empty()))


# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print ("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)
#
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
#
# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
#
# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
#
# # 等待队列清空
# while not workQueue.empty():
#     pass
#
# # 通知线程是时候退出
# exitFlag = 1
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")