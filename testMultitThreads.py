#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import queue
import threading
import time

exitFlag=0
threadLock = threading.Lock()

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print("thread start:%s" % self.name)
        # print_time(self.name,self.counter,5)
        process_data(self.name,self.counter)
        print("thread exit:%s" % self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print('%s: %s' % (threadName,time.ctime(time.time())))
        counter-=1

def process_data(threadNmae,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data=q.get()
            queueLock.release()
            print("%s pressing %s"%(threadNmae,data))
        else:
            queueLock.release()
        time.sleep(1)

threadList=["Thread-1","Thread-2","Thread-3"]
nameList=["one","two","three","four","five"]
queueLock=threading.Lock()
workQueue=queue.Queue(10)
threads=[]
threadID=1
'''
for tName in threadList:
    thread=myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag=1

for t in threads:
    t.join()

print("exit main thread!")
'''


# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)
# print(time.strftime("%Y%m%d %H:%M:%S",time.localtime()))
# print(time.mktime(time.strptime(localtime,"%a %b %d %H:%M:%S %Y")))


# str=input("please input something")
# if str.isdigit():
#     print("输入内容合法！")
# else:
#     print("支付数字不合法！请重新输入。")
#     str=input("please input something")


import random
goods={'A':149,'B':150,'C':120,'D':1400}
key=random.sample(goods.keys(),1)
print(key)
price=goods[key[0]]
print(type(price))
print("{:s} is random.You can gauss its price!".format(key[0]))
lockN=0
while(lockN<2):
    str = input("please input something")
    if not str.isdigit():
        print("the  price is illegal!please try again!")

    elif int(str)<price:
        print("lower than it!")

    elif int(str)==price:
        print("the right price")
        break
    elif int(str)>price:
        print("higher than it!")
    lockN+=1
else:
    print("You have no chance!")