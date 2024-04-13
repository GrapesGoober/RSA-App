from Protocol import chat_tcp

IP = "127.0.0.1"
PORT = 5000

mode = input("enter mode - new chatroom (n), connect (c)")
to_send: list[bytes] = []
to_receive: list[bytes] = []
match mode:
    case 'n':
        conn = chat_tcp.start_server("127.0.0.1", 5000)
        chat_tcp.start_chat_sync(conn, to_send, to_receive)
    case 'c':
        conn = chat_tcp.connect_server("127.0.0.1", 5000)
        chat_tcp.start_chat_sync(conn, to_send, to_receive)
    case _: exit()

# create a background thread to print from received queue
import threading
def print_messages():
    while True:
        while to_receive:
            print(to_receive.pop(0))
threading.Thread(target=print_messages, daemon=True).start()

# handle user inputs
while True:
    if m := input():
        to_send.append(m.encode())
