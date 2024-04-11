def secure_TCP_chatroom():
    while True:
        print(""" 
Welcome to secure TCP chatroom.
    1 - Change Keys
    2 - Create New Chatroom
    3 - Connect Chatroom
    4 - Exit
Press Number You Wanna Do: """)

        match input():
            case "1": change_keys()
            case "2": create_chatroom()
            case "3": connect_chatroom()
            case "4": exit(0)
            case _:   print("invalid inputs")

def change_keys():
    return

def create_chatroom():
    return

def connect_chatroom():
    return