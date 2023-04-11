from socket import *
import random

port = 2500
BUFSIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(10)
print('device_1 server is running...')

while True:
    conn, addr = sock.accept()
    print('connect from', addr)
    
    data = conn.recv(BUFSIZE).decode()
    temp = random.randint(0,40) #온도
    humi = random.randint(0,100) #습도
    light = random.randint(70,150) #조도
    message = str(temp) + ' ' + str(humi) + ' ' + str(light)
    
    if data == 'quit':
        break
    else:
        conn.send(message.encode())

    
conn.close()
sock.close()