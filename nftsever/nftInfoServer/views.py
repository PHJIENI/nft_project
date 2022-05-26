from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import logging
import threading
import time
from . import  getInfo
from .config import goods,ts
from .proThread import getInfoThread, consumerThread
logger = logging.getLogger('log')

def index(request):
    return HttpResponse("hello world")


"""
以下是线上运行的代码需要屏蔽
"""
print("开始创建监控任务")
threadId = 1
for t in ts:
    thread = getInfoThread(threadId,t)
    thread.start()
    threadId += 1
consumerThread()



