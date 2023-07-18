import socket
import sys

ADDRESS = sys.argv[1]
PORT = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ADDRESS, PORT))

to_server =''
while True:
    to_server = input("Enter message: ")
    client.send(to_server.encode())

    if(to_server == 'terminate'):
        client.close()
