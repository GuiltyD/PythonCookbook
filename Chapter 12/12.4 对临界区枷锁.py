#对临界区枷锁避免竞态条件
import threading
import time
class SharedCounter:
    def __init__(self,initial_value = 0):
        self.initial_value = initial_value
        self._value_lock = threading.Lock()
    
    def incr(self):
        #使用with语句可以保证同一时间只有一个线程在运行，避免了又增加又减少的情况
        time.sleep(5)
        with self._value_lock:
            print('自增1')
            self.initial_value+=1
            print('值为{}'.format(self.initial_value))
    
    def decr(self):
        with self._value_lock:
            print('自减2')
            self.initial_value-=2
            print('值为{}'.format(self.initial_value))
    

s =SharedCounter()

for i in range(10):
    increase = threading.Thread(target = s.incr)
    decrease = threading.Thread(target = s.decr)
    increase.start()
    decrease.start()

print(s.initial_value)
