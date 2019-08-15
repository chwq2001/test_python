import multiprocessing,time
def f(conn):
    print('(%s) 进程开始发送数据...' % multiprocessing.current_process().pid)
    # 使用conn发送数据
    conn.send('Python')
    time.sleep(3)
    conn.send('Python3')

if __name__ == '__main__':
    # 创建Pipe，该函数返回两个PipeConnection对象
    parent_conn, child_conn = multiprocessing.Pipe()
    # 创建子进程
    p = multiprocessing.Process(target=f, args=(child_conn, ))
    # 启动子进程
    p.start()
    print('(%s) 进程开始接收数据...' % multiprocessing.current_process().pid)
    # 通过conn读取数据
    print(parent_conn.recv())  # Python
    print(parent_conn.recv())
    p.join()