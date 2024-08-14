import threading
from threading import Thread, Lock
import time

ticket = 50
lock = Lock()  # 创建锁对象


def sal_ticket():
    global ticket
    for i in range(100):
        lock.acquire()  # 上锁
        if ticket > 0:
            print(f'{threading.current_thread().name}正在出售第{ticket}张票')
            ticket -= 1
        time.sleep(1)
        lock.release()  # 释放锁


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=sal_ticket)
        t.start()
