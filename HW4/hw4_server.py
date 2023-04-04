from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

def calculator(n1, n2, a):
    result = 0
    if a == '+':
        result = int(n1) + int(n2)
    elif a == '-':
        result = int(n1) - int(n2)  
    elif a == '*':
        result = int(n1) * int(n2)
    elif a == '/':
        num = int(n1) / int(n2)
        result = round(num,1)
    else:
        pass
    
    return result


while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            num = data.decode()
            str_num = num.split()
            cal = calculator(str_num[0], str_num[2], str_num[1])
            cal_result = str(cal)
        except:
            client.send(b'Try again')
        else:
            client.send(cal_result.encode())       
    client.close()
            
    
    
    