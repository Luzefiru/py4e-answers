import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

inp = input('Please enter a URL: ')
split_inp = inp.split('/')

# print(inp)

try:
    mysock.connect((split_inp[2], 80))
except:
    print('Please enter a valid URL.')
    exit()

cmd = f'GET {inp} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

stringdata = []
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    parsed_data = data.decode()
    stringdata.append(parsed_data)

mysock.close()

stringdata = ''.join(stringdata)
pos = stringdata.find('\r\n\r\n')
print(stringdata[pos:])