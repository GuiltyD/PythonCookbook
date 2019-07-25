from concurrent import futures
import time
def add1 (x):
    time.sleep(1)
    return x+1

res = []
# 一定要加这句话
if __name__ == "__main__":
    s = time.time()
    def when_done(r):
        res.append(r.result())
        print('Got:',r.result())
    with futures.ProcessPoolExecutor(4) as pool:
    #     for i in pool.map(add1,range(10)):
    #         print(i)
    #         res.append(i)
    # print(res)
        for i in range(10):
            funture_res = pool.submit(add1,i)
            funture_res.add_done_callback(when_done)#这个方法阻塞了进程
    print(res)
    e = time.time()
    print(e -s )