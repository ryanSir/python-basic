from multiprocessing import Pool
import os, time


def task(name):
    print(f'子进程的PID:{os.getpid()},执行的任务:{name}')
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print('父进程开始执行')
    # 创建进程池
    p = Pool(3)
    for i in range(10):
        # 以非阻塞的方式
        p.apply_async(func=task, args=(i,))

    p.close()  # 关闭进程池，不再接受新的任务
    p.join()  # 阻塞主进程，等待所有的子进程完成任务
    print('所有的子进程执行完毕,父进程执行结束')
    print(time.time() - start)
