import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

inp = input('Please enter a URL: ')
split_inp = inp.split('/')

# print(split_inp)

try:
    mysock.connect((split_inp[2], 80))
except:
    print('ERROR: Invalid URL!')
    exit()

cmd = f'GET {inp} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

count = 0
while True:
    data = mysock.recv(500)
    count = count + len(data)
    if len(data) < 1:
        break
    elif count >= 3000:
        break
    print(data.decode(),end='')

mysock.close()

print(f'\nTotal number of characters/bytes = {count}')