from socket import *
import random

port = 5000
BUFSIZE = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(10)
print('device_2 server is running...')

while True:
    conn, addr = sock.accept()
    print('connect from', addr)

    heart = random.randint(40,140) #심박수
    step = random.randint(2000,6000) #걸음수
    calorie = random.randint(1000,4000) #소모 칼로리
    message = str(heart) + ' ' + str(step) + ' ' + str(calorie)

    data = conn.recv(BUFSIZE).decode()
    
    if data == 'quit':
        break
    else:
        conn.send(message.encode())
    
   

    
    
    
conn.close()
sock.close()