from Protocol import server_chatroom, ClientChatroom

chatroom_IP = "127.0.0.1"
chatroom_PORT = 5000

server_chatroom.start_chatroom(chatroom_IP, chatroom_PORT)

while True:
    m = input()
    if not server_chatroom.is_running: break
    if m == "END": 
        server_chatroom.is_running = False
        break
    server_chatroom.messages.append(m.encode())