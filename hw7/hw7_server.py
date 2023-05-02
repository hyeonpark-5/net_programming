from socket import *
import threading
import time
port = 3333
BUFFSIZE = 1024

clients = []
                
def recv(sock):
    while True:
        data = sock.recv(BUFFSIZE)
      
        if 'quit' in data.decode():
            if sock in clients:
                print(addr, 'exited')
                clients.remove(sock)
                continue
        
        if sock not in clients:
            print('new client', addr)
            clients.append(sock)
        
        print(time.asctime() + str(addr) + ':' + data.decode())
        
        for client in clients:
            if client != sock:
                client.send(data)

      
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)
print('Server Started')

while True:
    conn, addr = s.accept()
    recvth = threading.Thread(target=recv, args=(conn,))
    recvth.start()
    
