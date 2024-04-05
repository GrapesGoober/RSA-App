import socket, threading

my_IP = "192.168.204.219"
my_port = 5005
receive_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_sock.bind((my_IP, my_port))

dest_IP = "192.168.204.206"
dest_port = 5005
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive():
    while True:
        data, addr = receive_sock.recvfrom(1024) # buffer size is 1024 bytes
        print(data)

def send():    
    while True:
        message = input().encode()
        send_sock.sendto(message, (dest_IP, dest_port))

receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()