#!/usr/bin/python3
# -*- coding: utf-8 -*-
#队列数据仅有一份取走了就没有了
import queue
#last in first out
q=queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
print(q.get_nowait())
print(q.get_nowait())
print(q.get_nowait())

#设置优先级
q1=queue.PriorityQueue()
q1.put("yiruiduan",-1)
q1.put("zhangye",3)
q1.put("yinuo",10)
print(q1.get_nowait())
print(q1.get_nowait())
print(q1.get_nowait())
