from Protocol import SocketUDP

IP = "127.0.0.1"
PORT_A = 5004
PORT_B = 5005

sock = SocketUDP(IP, PORT_A, IP, PORT_B)
sock.create_sockets()

while True:
    message = input("> ").encode()
    if message == b"END":
        break
    sock.send(message)

sock.print_log()