import time
def countdown(n):
    while n>0:
        print('T-mins:',n)
        yield 
        time.sleep(5)
        n-=1
    print('Blashoff!')

def countup(n):
    x = 0
    while x<n:
        print('T-add:',x)
        yield 
        time.sleep(1)
        x+=1
    print('Add Over!')

from collections import deque

class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()
    
    def new_task(self,task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                print('{} is Done!'.format(task.__name__))

t =TaskScheduler()
t.new_task(countdown(10))
t.new_task(countup(15))
t.new_task(countdown(20))
t.run()