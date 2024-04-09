from Protocol import ServerChatroom, ClientChatroom

chatroom_IP = "127.0.0.1"
chatroom_PORT = 5000

#s = ServerChatroom(chatroom_IP, chatroom_PORT)
s = ClientChatroom(chatroom_IP, chatroom_PORT)

while True:
    m = input()

    if not s.is_alive: break
    if m == "END": 
        s.terminate()
        break

    if m == "LOG":
        for i in s.message_log: print(i)
        continue

    s.send(m.encode())