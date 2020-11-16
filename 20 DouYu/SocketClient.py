'''
Socket 客户端
'''
import asyncore
import sys


# 1. 定义类并继承自 asyncore.dispatcher
class SocketClient(asyncore.dispatcher):
    def __init__(self, host, port):
        # 调用父类构造器
        asyncore.dispatcher.__init__(self)
        # 创建Socket对象
        self.create_socket()
        # 连接服务器
        address = (host, port)
        self.connect(address)

    # Socket 连接之后 回调此函数
    def handle_connect(self):
        print('连接成功')

    def writable(self):
        return False

    # 当有数据需要发送时，此函数会被触发
    def handle_write(self):
        self.send('qwq'.encode('utf-8'))

    # 是否有数据需要从服务器读取，为True时会触发handle_read函数
    def readable(self):
        return True

    def handle_read(self):
        result = self.recv(1024)
        print(result)

    # 当函数运行过程中发生异常时回调
    def handle_error(self):
        # 编写处理错误方法
        t, e, trace = sys.exc_info()
        print(t, e, trace)

    # 当连接被关闭时触发该函数
    def handle_close(self):
        print("连接关闭")
        self.close()


if __name__ == '__main__':
    client = SocketClient('127.0.0.1', 9000)
    # 开始启动运行循环
    asyncore.loop(timeout=5)
