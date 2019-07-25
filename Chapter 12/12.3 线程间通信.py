import heapq
import threading
import time


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        self._cv = threading.Condition()

    def put(self,item,priority):
        with self._cv:
            heapq.heappush(self._queue,[-priority,self._index,item])
            self._index +=1
            print('生产者线程已经生产一个值{},现在线程挂起'.format(item))
            self._cv.notify()
    
    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                print('生产者线程商品已经消耗完毕，现在消费者线程处于挂起状态')
                self._cv.wait()
            print('消费者线程启动，开始处理值，得到值{}'.format(heapq.heappop(self._queue)[-1]))
    
    def __len__(self):
        return len(self._queue)

sign = True
priority = PriorityQueue()
def productor():
    global sign
    for i,j in zip(list(range(10)),list(range(10))[::-1]):
        time.sleep(0.5)
        priority.put(i,j)
    sign =False

def consumer():
    while sign:
        time.sleep(0.5)
        priority.get()

p = threading.Thread(target = productor)
c = threading.Thread(target = consumer)
p.start()
c.start()
p.join()
c.join()



             
