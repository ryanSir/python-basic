import threading
from threading import Thread
import time


class SubThread(Thread):
    def run(self):
        for i in range(3):
            print(f'线程：{threading.current_thread().name}正在执行{i}')


if __name__ == '__main__':
    print('主线程开始执行')
    lst = [SubThread() for i in range(2)]
    for item in lst:
        item.start()  # 启动线程

    for item in lst:
        item.join()  # 阻塞主线程

    print('主线程执行完毕')
