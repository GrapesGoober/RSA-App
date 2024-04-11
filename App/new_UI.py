import json
from RSA import generate_keys,encrypt,decrypt
from Protocol import Chatroom

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
    print("The minimum key size is 256")
    size = int(input("Enter keys size: "))
    if size < 256:
        print("Too small! Try again")
        change_keys()
    else:
        pub,priv = generate_keys(size)
    return

def create_chatroom():
    my_IP = input("Enter IP: ")
    my_PORT = int(input("Enter Port: "))
    chatroom = Chatroom(mode='server', ip=my_IP, port=my_PORT)
    return

def connect_chatroom():
    dest_IP = input("Enter IP: ")
    dest_PORT = int(input("Enter Port: "))
    chatroom = Chatroom(mode='client', ip=dest_IP, port=dest_PORT)
    return