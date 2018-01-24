import socket


class ClientBase():
    HOST = "pawel-pc"
    PORT = 7001

    def __init__(self,s=None):
        if s is None:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.s = s


    def sendmsg(self, port, client):
        self.port = port
        self.s.connect((self.HOST, self.port))
        msg = input("c: ")
        self.s.sendall(client.encode())
        self.s.sendall(msg.encode())
        self.s.close()

    def receive(self, port, client):
        self.port = port
        self.s.connect((self.HOST, self.port))
        self.s.sendall(client.encode())
        msg_received = self.s.recv(1024)
        print("fs: {}".format(msg_received))
        self.s.close()
