import socket, select                                                                                                                                

host = '127.0.0.1'
port = 5000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
inout = [socket]

while True:
    infds, outfds, errfds = select.select(inout, inout, [], 5)
    if infds:
        buf = socket.recv(1024)
        if len(buf) != 0:
            print('receive data:', buf)
    if outfds:
        socket.sendall(b"python select client from Debian.\n")