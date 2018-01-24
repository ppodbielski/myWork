from server_base import ServerBase

from chat_menu import ChatMenu

menu = ChatMenu()

if __name__=="__main__":


        server1 = ServerBase()
        server2 = ServerBase()

        #server1.establish(7003)
        msg = server1.receive(7003)

        #server2.establish(7004)
        server2.send(7004, msg.decode())
