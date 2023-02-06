import socket

class Network:
    def __int__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.3"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()

        