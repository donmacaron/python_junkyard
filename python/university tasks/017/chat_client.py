import socket

s = socket.socket()
host = 'localhost'
port = 9090

s.connect((host, port))
print('connected to ', host)

while(True):
    z = input('>>> ')
    s.send(z.encode('UTF-8'))
    print(s.recv(1024))
