from socket import *
import time
BUF_SIZE = 1024
clock = time.asctime()
s1 = socket(AF_INET, SOCK_STREAM)
s2 = socket(AF_INET, SOCK_STREAM)

# s1.connect(('localhost', 2500))
# s2.connect(('localhost', 5000))


while True:
    msg = input("Request: ")
    print(msg)
    if msg == '1':
        s1 = socket(AF_INET, SOCK_STREAM)
        s1.connect(('localhost', 2500))

        s1.send(b"1")
        data1 = s1.recv(BUF_SIZE).decode()
        s = data1.split()
        file_msg = clock + ': device1: ' + 'Temp=' + s[0] + ' Humid=' + s[1] + ' ilum=' + s[2] + '\n'
        print(file_msg)
        f = open('./data.txt','a')
        f.write(file_msg)
        f.close()
        s1.close()
    elif msg == '2':
        s2 = socket(AF_INET, SOCK_STREAM)
        s2.connect(('localhost', 5000))
        s2.send(b"2")
        data2 = s2.recv(BUF_SIZE).decode()
        s = data2.split()
        file_msg = clock + ': device2: ' + 'Heartbeat=' + s[0] + ' Steps=' + s[1] + ' Cal=' + s[2] + '\n'
        print(file_msg)
        f = open('./data.txt','a')
        f.write(file_msg)
        f.close()
        s2.close()
    elif msg == 'quit':
        q = 'quit'
        s1 = socket(AF_INET, SOCK_STREAM)
        s1.connect(('localhost', 2500))
        s2 = socket(AF_INET, SOCK_STREAM)
        s2.connect(('localhost', 5000))
        
        s1.send(q.encode())
        s2.send(q.encode())
        s1.close()
        s2.close()

    else:
        pass
        

        
    

        