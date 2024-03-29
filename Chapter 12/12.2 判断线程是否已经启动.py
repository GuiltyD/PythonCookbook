from threading import Condition,Thread
import time

class PeriodicTimer:
    def __init__(self,interval):
        self._interval = interval
        self._flag = 0
        self._cv = Condition()
    def start(self):
        t = Thread(target = self.run)
        t.daemon = True
        t.start()
    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^=1
                self._cv.notify_all()
    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

ptimer = PeriodicTimer(5)
ptimer.start()


def countdown(n):
    while n>0:
        # ptimer.wait_for_tick()
        print('m-min',n)
        n-=1
         
def countup(last):
    n = 0
    while n<last:
        # ptimer.wait_for_tick()
        print('m-up',n)
        n+=1

# print(0^1)
Thread(target = countdown,args=(10,)).start()
Thread(target = countup,args=(5,)).start()