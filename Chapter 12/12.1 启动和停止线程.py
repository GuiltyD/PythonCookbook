import time
from threading import Thread

class CountdownTask:
    def __init__(self,n):
        self._running= True
        self.n = n 
    
    def terminate(self):
        self._running = False
    
    def run(self):
        while self._running and self.n>0:
            print('T-minus',self.n)
            self.n-=1
            time.sleep(2)

c = CountdownTask(5)
t = Thread(target = c.run)
start = time.time()
t.start()
print('Process start sleep')
time.sleep(15)
c.terminate()
print(c.n)
end = time.time()
t.join()
print(end-start)
