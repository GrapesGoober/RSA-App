from Protocol import Chatroom

chatroom_IP = "127.0.0.1"
chatroom_PORT = 5000

mode = input("enter mode - new chatroom (n), connect chatroom (c): ")
chatroom = None
match mode:
        
    case 'n':
        chatroom = Chatroom(mode='server', ip='127.0.0.1', port=5000)
    case 'c':
        chatroom = Chatroom(mode='client', ip='127.0.0.1', port=5000)

while True:
    m = input()
    if not chatroom.is_running: break
    if m == "END": 
        chatroom.is_running = False
        break
    chatroom.messages.append(m.encode())