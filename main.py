from Protocol import chat_tcp

chatroom_IP = "127.0.0.1"
chatroom_PORT = 5000

mode = input("enter mode - new chatroom (n), connect (c)")
match mode:
    case 'n':
        chat_tcp.start_server("127.0.0.1", 5000)
        chat_tcp.start_chat_sync()
    case 'c':
        chat_tcp.connect_server("127.0.0.1", 5000)
        chat_tcp.start_chat_sync()
    case _: exit()

# create a background thread to print from received queue
import threading
def print_messages():
    while True:
        while chat_tcp.received:
            print(chat_tcp.received.pop(0))
threading.Thread(target=print_messages, daemon=True).start()

# handle user inputs
while True:
    if m := input():
        chat_tcp.to_send.append(m.encode())
