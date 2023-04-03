import socket
sock = socket.socket(socket.AF_INET, 
socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

name = "박가현"
sock.send(name.encode())
num = sock.recv(1024)
number = int.from_bytes(num,"big")
print(number)

sock.close()