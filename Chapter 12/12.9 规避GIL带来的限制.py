import multiprocessing
import time


def add1(x):
    time.sleep(1)
    return x+1
res = []
if __name__ == '__main__':
    def when_done(r):
        res.append(r.get())
    pool = multiprocessing.Pool()
    s = time.time()
    for i in range(10):
        a = pool.apply_async(add1,(i,),callback = when_done)

    e = time.time()
    print(res)
    print(e-s)
