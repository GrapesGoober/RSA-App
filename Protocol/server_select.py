import select, socket, threading

class ServerChatroom:
    def __init__(self, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        self.sock.bind(("127.0.0.1", port))
        self.sock.listen()
        self.inputs = [ self.sock ]
        self.messages = [ ] # outgoing message queue
        self.conn = None
        self.is_running = True
        chatroom_thread = threading.Thread(target=self.__chatroom_thread)
        chatroom_thread.start()

    def __chatroom_thread(self):
        while self.is_running:
            readable, writable, _ = select.select(self.inputs, self.inputs, [])
            for s in readable:
                if s is self.sock:
                    conn, addr = s.accept()
                    print(f"connected from {addr}")
                    self.inputs.append(conn)
                else: 
                    data = s.recv(1024)
                    if data:
                        print(data)
                    if not data:
                        print("THIS CHATROOM IS TERMINATED")
                        self.sock.close()
                        return
            for s in writable:
                if self.messages:
                    s.sendall(self.messages[0]) 
                    self.messages.pop(0)
        self.server.close()


chat = ServerChatroom(5000)

while True:
    m = input()

    if m == "END": 
        is_running = False
        break

    # if m == "LOG":
    #     for i in s.message_log: print(i)
    #     continue

    chat.messages.append(m.encode())

