from Protocol import run_chatroom, ClientChatroom, sync_chatroom

chatroom_IP = "127.0.0.1"
chatroom_PORT = 5000

mode = input("enter mode - new chatroom (n), connect (c), sync (s): ")
match mode:
    case 'n':
        if __name__ == "__main__":
            run_chatroom("127.0.0.1", 5000)
    case 'c':
        chatroom = ClientChatroom()
        chatroom.connect("127.0.0.1", 5000)
        while m := input():
            chatroom.send_message(m.encode())
        chatroom.disconnects()
    case 's':
        sync_chatroom("127.0.0.1", 5000)
