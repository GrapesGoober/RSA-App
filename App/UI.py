import json

from Protocol import Receiver, Sender
from RSA import generate_keys

def start_program():
    while True:
        print(""" 
Welcome to Data tranfering program.
    1 - Chatting
    2 - Tranfering file
    3 - Exit
Press Number You Wanna Do: """)

        match input():
            case "1": Chatroom()
            case "2": secure_file_tranfer()
            case "3": exit(0)
            case _:   print("invalid inputs")

def secure_file_tranfer():
    print(""" 
Secure file tranfering program.
    1 - Sending File
    2 - Recieving file
    3 - Return
Press Select your activity: """)

    match input():
        case "1": sending()
        case "2": recieving()
        case "3": start_program()
        case _:   print("invalid inputs")

def enterIP():
    IP = input("Enter IP:")
    PORT = int(input("Enter Port: "))
    return IP, PORT

def reading_key():
    with open("App\\config.json", "r") as f:
        config = json.loads(f.read())
    key = config["keys"]
    return key

def sending():
    IP, Port = enterIP()
    path = input("Enter file path: ")
    name = input("Recipient Username: ")
    with Sender(IP, Port, name) as r:
            with open(path, "rb") as f:
                while m := f.read(1024): r.send(m)

def recieving():
    IP, Port = enterIP()
    print(f"server awaiting connection")
    with Receiver(IP, Port) as r:
        print(f"connected")
        with open("Test Files\\random_bytes_receive.bin", "wb") as f:
            while m := r.get_message(): f.write(m)
    print(f"done")

def Chatroom():
    print(""" 
Secure messaging program.
    1 - Sending
    2 - Recieving
    3 - Return
Press Select your activity: """)

    match input():
        case "1": message_sending()
        case "2": message_recieving()
        case "3": start_program()
        case _:   print("invalid inputs")
        
def message_sending():
    name = input("Recipient Username: ")
    IP, Port = enterIP()
    with Sender(IP, Port, name) as r:
        while m := input("> "): r.send(m.encode())

def message_recieving():
    IP, Port = enterIP()
    print(f"server awaiting connection")
    with Receiver(IP, Port) as r:
        print(f"connected")
        while m := r.get_message(): print(m.decode())