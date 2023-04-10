from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
   
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    head = req[0]
    name = head.split()
    file = name[1]
    filename = file[1:]
 
    try: 
        if filename == 'index.html':
            f = open(filename, 'r', encoding='utf-8')
            mimeType = 'text/html'
        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
        
        header = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: ' + mimeType + '\r\n' + '\r\n'
        c.send(header.encode('utf-8'))
        data = f.read()
        if filename == 'index.html':
            c.send(data.encode('euc-kr'))
        else:
            c.send(data)
            
    except Exception as e:
        header = 'HTTP/1.1 404 NoT Found\r\n' + '\r\n'
        response = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>\n' +  '<BODY>Not Found</BODY></HTML>'
        header += response
        c.send(header.encode('utf-8'))
        
   
    c.close()