import select, socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server_address = ('127.0.0.1', 5000)
server.bind(server_address)
server.listen()
inputs = [ server ]
messages = [ ] # outgoing message queue
conn = None
is_running = True
def chatroom_loop():
    while is_running:
        readable, writable, _ = select.select(inputs, inputs, [])

        for s in readable:
            if s is server:
                conn, addr = s.accept()
                print(f"connected from {addr}")
                inputs.append(conn)
            else: 
                data = s.recv(1024)
                if data:
                    print(data)
                if not data:
                    print("THIS CHATROOM IS TERMINATED")
                    server.close()
                    return
        for fds in writable:
            if messages:
                fds.sendall(messages[0]) 
                messages.pop(0)
    
    server.close()

chatroom_thread = threading.Thread(target=chatroom_loop)
chatroom_thread.start()


while True:
    m = input()

    if m == "END": 
        is_running = False
        break

    # if m == "LOG":
    #     for i in s.message_log: print(i)
    #     continue

    messages.append(m.encode())

