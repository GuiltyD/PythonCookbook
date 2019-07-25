import queue
from threading import Thread,Event
import time

class ActorExit(Exception):
    pass

class Actor:
    def __init__(self):
        self.mailbox = queue.Queue()
    
    def send(self,msg):
        print('发送消息{}到消息队列'.format(msg))
        self.mailbox.put(msg)

    def recv(self):
        msg = self.mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg
    
    def close(self):
        self.send(ActorExit)
        print('消息队列任务接收完毕')
    
    def start(self):
        print('启动消息队列执行任务')
        self._terminate = Event()
        t = Thread(target = self._bootstrap)
        t.daemon =True
        t.start()
    
    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            print('收到终止信号，挂起线程，等待主线程退出')
        finally:
            self._terminate.set()

    def join(self):
        self._terminate.wait()
    
    def run(self):
        while True:
            msg = self.recv()
        
class PrintActor(Actor):
    def __init__(self):
        super().__init__()
        self.count = 0
    def run(self):
        while True:
            
            msg = self.recv()
            if msg is not ActorExit:
                self.count += 1
               
                time.sleep(2)
                print('正在执行消息队列中的任务，请稍后.......')
                print('Got[{}]:{}'.format(self.count,msg))

p = PrintActor()
p.start()
p.send('Hello')
p.send('World')
p.close()
p.join()

