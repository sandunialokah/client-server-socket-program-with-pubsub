import socket
import sys
from _thread import *

ADDRESS = '127.0.0.1'
PORT = int(sys.argv[1])
THREAD_COUNT = 0


def client_handler(conn):
    conn.send(str.encode('You are now connected'))
    while True:
        data = conn.recv(2048)
        message = data.decode('utf-8')
        if(message == ' terminate'):
            break
        reply = f'Server: {message}'
        print(message)
        conn.sendall(str.encode(reply))
    conn.close()
    
def accept_connections(server):
    conn,addr = server.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(client_handler, (conn, ))
    

def start_server():
    server = socket.socket()
    server.bind((ADDRESS, PORT))
    server.listen(5)
    
    while True:
        accept_connections(server)


start_server()

# server = socket.socket()
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.bind((ADDRESS, PORT))
# server.listen(5)
# conn,addr = server.accept()

# from_client = ''
# while True:
#         data = conn.recv(1024)
#         if not data: break
#         from_client = data.decode()
#         print(from_client)
#         # conn.send("I am SERVER\n".encode())
#         if(from_client == 'terminate'):
#             conn.close() 

    
# print('client disconnected and shutdown')