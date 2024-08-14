import time
from multiprocessing import Process

import os


def test():
    print(f'我是子进程，我的IP是：{os.getpid()},我的父进程是:{os.getppid()}')
    time.sleep(1)


if __name__ == '__main__':
    print('主进程开始执行')
    lst = []

    for i in range(5):
        # 创建子进程
        p = Process(target=test)
        # 启动子进程
        p.start()
        # 启动中的进程添加到列表中
        lst.append(p)
    # 遍历列表，列表中的五个子进程
    for item in lst:
        item.join() # 阻塞主进程
    print('主进程执行结束')
