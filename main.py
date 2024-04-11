from Protocol import Chatroom
import threading

chatroom_IP = "127.0.0.1"
chatroom_PORT = 5000

mode = input("enter mode - new chatroom (n), connect chatroom (c): ")
chatroom = None
match mode:
    case 'n':
        chatroom = Chatroom(mode='server', ip='127.0.0.1', port=5000)
    case 'c':
        chatroom = Chatroom(mode='client', ip='127.0.0.1', port=5000)

## Setup a message-printing thread
def display_message_thread():
    # WHY IS THIS CAUSING THEADS EXCEPTIONS?!?! IT'S JUST A MESSAGE QUEUE!!!
    # while True:
    while chatroom.is_running:
        for m in chatroom.receive():
            print(m.decode())
threading.Thread(target=display_message_thread, daemon=True).start()

while True:
    m = input()
    if not chatroom.is_running: break
    if m == "END": 
        chatroom.is_running = False
        break
    chatroom.send(m.encode())