import socket, threading, select, RSA
from typing import Generator
from Protocol.keys import Apriv, Apub, Bpriv, Bpub

class Chatroom:

    messages_out: list[bytes]   = [ ]
    messages_in: list[bytes]    = [ ]
    is_running: bool            = False
    sock: socket.socket         = None
    inout: list[any]            = [ ] # io list for the select library

    encrypt_key = None
    decrypt_key = None

    def __init__(self, mode: str, ip: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_running = True
        match mode:
            case "server": self.start_server(ip, port)
            case "client": self.connect_server(ip, port)
            case _: 
                raise Exception("Chatroom mode supports only 'server' and 'client'")
            
    def send(self, message: bytes) -> None:
        self.messages_out.append(message)

    def receive(self) -> Generator[bytes, None, None]:
        while self.messages_in:
            yield self.messages_in.pop(0)
        
    def start_server(self, ip: str, port: int) -> None:
        self.sock.bind((ip, port))
        self.sock.listen()
        chatroom = threading.Thread(target=self.await_conn_then_chat)
        chatroom.start()

        self.encrypt_key = Bpub
        self.decrypt_key = Apriv

    def connect_server(self, ip: str, port: int) -> None:
        self.sock.connect((ip, port))
        self.inout.append(self.sock)
        chatroom = threading.Thread(target=self.handle_chat)
        chatroom.start()

        self.encrypt_key = Apub
        self.decrypt_key = Bpriv

    def await_conn_then_chat(self):
        # receive connection first
        conn, addr = self.sock.accept()
        self.messages_in.append(f"connected from {addr}".encode())
        self.inout.append(conn)
        # once the connection is established, start chatroom
        self.handle_chat()

    def handle_chat(self) -> None:
        while self.is_running:
            readable, writable, _ = select.select(self.inout, self.inout, [])
            for s in readable:
                data = s.recv(1024)
                if data:
                    self.messages_in.append(RSA.decrypt(data, self.decrypt_key))
                if not data:
                    self.messages_in.append(b"THIS CHATROOM IS TERMINATED")
                    self.sock.close()
                    self.is_running = False
                    return
            for s in writable:
                if self.messages_out:
                    s.sendall(RSA.encrypt(self.messages_out[0], self.encrypt_key)) 
                    self.messages_out.pop(0)
        self.sock.close()