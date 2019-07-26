from collections import defaultdict
class PaperPublisher:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self,newsub,typeof = None):
        if typeof is None:
            self.subscribers['all'].append(newsub)
        else:
            self.subscribers[typeof].append(newsub)
    
    def unsubscribe(self,sub,typeof=None):
        if typeof is None:
            typeof = 'all'
        for i in self.subscribers[typeof]:
                if i == sub:
                    self.subscribers['all'].remove(sub)
    
    def publish(self,value,typeof = None):
        for i in self.subscribers[typeof]:
            i.send(value,typeof)
        for i in self.subscribers['all']:
            i.send(value,typeof)
        
class Task:
    def send(self):
        pass


class XiaoMing(Task):
    def send(self,value,typeof):
        print('My name is XiaoMing,I am reading {} of {}.'.format(value,typeof))

class XiaoHong(Task):
    def send(self,value,typeof):
        print('My name is XiaoHong,I am reading {} of {}.'.format(value,typeof))


class XiaoJun(Task):
    def send(self,value,typeof):
        print('My name is XiaoJun,I am reading {} of {}.'.format(value,typeof))
p = PaperPublisher()
xiaoming = XiaoMing()
xiaohong = XiaoHong()
xiaojun = XiaoJun()
p.subscribe(xiaoming,'dailypaper')
p.subscribe(xiaohong,'Times')
p.subscribe(xiaojun)

p.publish('jintianshimaomao','dailypaper')

        