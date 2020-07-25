import socket

addr = '127.0.0.1'   # '127.0.0.122311'
try:
    socket.inet_aton(addr)
    print('valid ip')
except socket.error:
    print('invalid ip')