import socket, select, threading                                                                                                                                

messages = [ ] # outgoing message queue
is_running = False
sock: socket.socket = None
select_inout = [ ]

def connect_chatroom(ip: str, port: int):
    global sock, is_running
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    select_inout.append(sock)
    is_running = True
    chatroom = threading.Thread(target=chatroom_thread)
    chatroom.start()

def chatroom_thread():
    while is_running:
        readable, writable, _ = select.select(select_inout, select_inout, [])
        for s in readable:
            data = s.recv(1024)
            if data:
                print(data)
            if not data:
                print("THIS CHATROOM IS TERMINATED")
                sock.close()
                return
        for s in writable:
            if messages:
                s.sendall(messages[0]) 
                messages.pop(0)
    sock.close()

connect_chatroom("127.0.0.1", 5000)

while True:
    m = input()

    if m == "END": 
        is_running = False
        break

    # if m == "LOG":
    #     for i in s.message_log: print(i)
    #     continue

    messages.append(m.encode())
