import threading
import time
from contextlib import contextmanager

#死锁代码
applelock = threading.Lock()
orangelock = threading.Lock()
# def applefirst():
#     while True:
#         print('获取苹果锁')
#         applelock.acquire()
#         print('获取橘子锁')
#         orangelock.acquire()
#         print('释放苹果锁')
#         applelock.release()
#         print('释放橘子锁')
#         orangelock.release()
# def orangefirst():
#     while True:
#         print('获取橘子锁')
#         orangelock.acquire()
#         print('获取苹果锁')
#         applelock.acquire()
#         print('释放苹果锁')
#         orangelock.release()
#         print('释放橘子锁')
#         applelock.release()


# apple = threading.Thread(target = applefirst)
# orange = threading.Thread(target = orangefirst)
# apple.start()
# orange.start()


#解决死锁
_local = threading.local()
@contextmanager
def acquire(*locks):
    locks = sorted(locks,key = lambda x:id(x))
    acquired = getattr(_local,'acquired',[])
    if acquired and max(id(lock) for lock in acquired)>=id(locks[0]):
        raise RuntimeError('锁正在使用!')
    acquired.extend(locks)
    _local.aquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield 
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]

def applefirst():
    while True:
        with acquire(applelock,orangelock):
            print('获取苹果和橘子')
def orangefirst():
    while True:
        with acquire(orangelock,applelock):
            print('获取橘子和苹果')



apple = threading.Thread(target = applefirst)
orange = threading.Thread(target = orangefirst)
apple.start()
orange.start()