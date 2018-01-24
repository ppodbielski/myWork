import socket
import select
import threading

class ChatServer(object):



    def __init__(self,host,port,buffer):

        # init block, set up basic parameters, like host - if '' = any, listen port,
        # CONNECTION_LIST = table with input (network socket in this case)
        # set up startup options
        self.thread = []
        self.msg_list = []
        self.CONNECTION_LIST = []
        self.host = host
        self.port = port
        self.buffer = buffer
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host,self.port))

    def listen(self):

        #Listen method responsible for receive incoming connection and store incoming data

        self.server.listen(0)
        self.CONNECTION_LIST.append(self.server)

        while True:
            self.sock_read, self.sock_write, self.sock_except = select.select(self.CONNECTION_LIST, [], [])

            for sock in self.sock_read:
                if sock is self.server:
                    client, addr = self.server.accept()
                    self.CONNECTION_LIST.append(client)
                    self.thread.append(client)
                else:
                    data = client.recv(self.buffer)
                    if len(data) != 0:
                        self.msg_list.append(data)
                        print(self.msg_list)
                    else:
                        sock.close()
                        self.CONNECTION_LIST.remove(sock)
                        print(self.CONNECTION_LIST)
                        continue
        self.server.close()
        self.CONNECTION_LIST.remove(self.server)



if __name__ == '__main__':
    ChatServer('',7008,1024).listen()