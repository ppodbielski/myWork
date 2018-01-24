import socket
import datetime

port = 7008
host = 'pawel-pc'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

AUTH = ("Client 1:")


while 1:

    msg = input(":")
    if msg == "x":
        client_socket.close()
        break
    date = str(datetime.datetime.now())
    msg = date +' '+ AUTH +' '+ msg
    client_socket.sendall(msg.encode())
    #msg = client_socket.recv(1024)
    #print("recv: {}".format(msg))

