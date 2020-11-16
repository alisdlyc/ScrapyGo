import asyncore
import sys


class DouyuClient(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()

        address = (host, port)
        self.connect()

    def handle_connect(self):
        print("连接成功")

    def writable(self):
        return False

    def handle_write(self):
        pass

    def readable(self):
        return True

    def handle_read(self):
        result = self.recv(1024)
        print(result)

    def handle_error(self):
        t, e, trace = sys.exc_info()
        print(e)
        self.close()

    def handle_close(self):
        self.close()


if __name__ == '__main__':
    client = DouyuClient('openbarrage.douyutv.com', 8601)
    asyncore.loop(timeout=10)
