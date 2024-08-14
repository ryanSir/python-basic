from multiprocessing import Queue

if __name__ == '__main__':
    #  创建一个队列
    q = Queue(3)  # 最多可以接受3条信息
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    # 向队列中添加信息
    q.put('hello')
    q.put('world')
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    q.put('Python3')
    print('队列是否为空:', q.empty())
    print('队列是否为满:', q.full())
    # print('队列当中信息的个数:', q.qsize())

    # 出队列
    # print(q.get(), q.get(), q.get())
    # q.put_nowait('html')
    # q.put("sql")  # 不会报错，会一直等待，等待队列有空位置

    # 遍历
    while not q.empty():
            print(q.get_nowait())
