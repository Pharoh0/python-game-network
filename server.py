import socket
from _thread import *
import sys

server = "192.168.1.3"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect to server and port
    s.bind((server, port))
except socket.error as e:
    str(e)

# create connection and opin up the port
s.listen(2) # two people
print("Wating for a connection, Server Started")

def threaded_client(conn):
    reply = ""
    # continue loop while client still connecting
    while True:
        try:
            # receve information
            data = conn.revc(2048)
            # decode that data
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Receving: ", reply)
                print("Sending: ", reply)
            
            conn.sendall(str.encode(reply))
        except :
            break
    print("loss connection")    
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))