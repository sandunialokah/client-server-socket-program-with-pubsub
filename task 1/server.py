import socket
import sys

ADDRESS = '127.0.0.1'
PORT = int(sys.argv[1])

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ADDRESS, PORT))
server.listen(5)
conn,addr = server.accept()

from_client = ''
while True:
        data = conn.recv(1024)
        if not data: break
        from_client = data.decode()
        print(from_client)
        # conn.send("I am SERVER\n".encode())
        if(from_client == 'terminate'):
            conn.close() 

    
print('client disconnected and shutdown')