import json

from Protocol import Chatroom
from RSA import generate_keys

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
        pub, priv = generate_keys(size)
        with open("App\config.json", "r") as f:
            config = json.loads(f.read())
        try:
            config["k_pub"] = pub
            config["k_priv"] = priv
        except ValueError:
            print("Invalid input. Please enter a valid value.")
        with open("App\config.json", "w") as f:
            json.dump(config, f, indent=4)  # Write back to file with indentation

def create_chatroom():
    my_IP = input("Enter IP: ")
    my_PORT = int(input("Enter Port: "))
    chatroom = Chatroom(mode='server', ip=my_IP, port=my_PORT)

def connect_chatroom():
    dest_IP = input("Enter IP: ")
    dest_PORT = int(input("Enter Port: "))
    chatroom = Chatroom(mode='client', ip=dest_IP, port=dest_PORT)