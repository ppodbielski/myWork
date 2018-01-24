import socket

class ServerBase():
    HOST = ''
    PORT = 7001

    def __init__(self,s=None):
        if s is None:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.s = s

#    def establish(self, port):
#        self.port = port
#        self.s.bind((self.HOST, self.port))
#        self.s.listen(1)

    def receive(self, port):
        self.port = port
        self.s.bind((self.HOST, self.port))
        self.s.listen(1)
        (connection, address) = self.s.accept()
        print('Incoming from {}'.format(address))
        while 1:
            data = connection.recv(1024)
            if not data:
                break
            print("s: {}".format(data))
            return data

        connection.close()

    def send(self, port, msg_data):
        self.port = port
        self.s.bind((self.HOST, self.port))
        self.s.listen(1)
        (connection, address) = self.s.accept()
        print('Incoming from {}'.format(address))
        while 1:
            data = connection.recv(1024)
            if not data:
                break
            print("s: {}".format(data))
            connection.sendall(msg_data.encode())
            return data

        connection.close()
