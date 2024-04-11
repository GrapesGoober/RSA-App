from Protocol import start_chatroom, ClientChatroom

chatroom_IP = "127.0.0.1"
chatroom_PORT = 5000

mode = input("enter mode - new chatroom (n), connect chatroom (c): ")
chatroom = None
match mode:
    case 'n':
        if __name__ == "__main__":
            start_chatroom("127.0.0.1", 5000)
    case 'c':
        chatroom = ClientChatroom()
        chatroom.connect("127.0.0.1", 5000)
        while m := input():
            chatroom.send_message(m.encode())
        chatroom.disconnects()
