from Protocol import server_chatroom, client_chatroom

chatroom_IP = "127.0.0.1"
chatroom_PORT = 5000

mode = input("enter mode - new chatroom (n), connect chatroom (c): ")
chatroom = None
match mode:
    case 'n':
        server_chatroom.start_chatroom(chatroom_IP, chatroom_PORT)
        chatroom = server_chatroom
    case 'c':
        client_chatroom.connect_chatroom(chatroom_IP, chatroom_PORT)
        chatroom = client_chatroom

while True:
    m = input()
    if not chatroom.is_running: break
    if m == "END": 
        chatroom.is_running = False
        break
    chatroom.messages.append(m.encode())