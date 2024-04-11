import socket, threading, select

class Chatroom:

    messages: list[bytes]   = [ ] # outgoing message queue
    is_running: bool        = False
    sock: socket.socket     = None
    inout: list[any]        = [ ] # io list for the select library

    def __init__(self, mode: str, ip: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_running = True
        match mode:
            case "server": self.__start_server(ip, port)
            case "client": self.__connect_server(ip, port)
            case _: 
                raise Exception("Chatroom mode supports only 'server' and 'client'")
        
        chatroom = threading.Thread(target=self.__chatroom_message_thread)
        chatroom.start()
    
    def __start_server(self, ip: str, port: int) -> None:
            self.sock.bind((ip, port))
            self.sock.listen()
            # the server only accepts 1 connection, and is a blocking code
            conn, addr = self.sock.accept()
            print(f"connected from {addr}")
            self.inout.append(conn)

    def __connect_server(self, ip: str, port: int) -> None:
            self.sock.connect((ip, port))
            self.inout.append(self.sock)

    def __chatroom_message_thread(self) -> None:
        while self.is_running:
            readable, writable, _ = select.select(self.inout, self.inout, [])
            for s in readable:
                data = s.recv(1024)
                if data:
                    print(data)
                if not data:
                    print("THIS CHATROOM IS TERMINATED")
                    self.sock.close()
                    self.is_running = False
                    return
            for s in writable:
                if self.messages:
                    s.sendall(self.messages[0]) 
                    self.messages.pop(0)
        self.sock.close()
