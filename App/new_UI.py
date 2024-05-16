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

def create_key():
    print("The minimum key size is 256")
    size = int(input("Enter keys size: "))
    if size < 256:
        print("Too small! Try again")
        return create_key()
    else:
        keys = generate_keys(size)
        with open("App\\private_key.json", "r") as f:
            config = json.loads(f.read())
        try:
            config["keys"] = keys
        except ValueError:
            print("Invalid input. Please enter a valid value.")
        with open("App\\private_key.json", "w") as f:
            json.dump(config, f, indent=4)  # Write back to file with indentation
        user = input("Enter Username: ")
        data = {user:keys[1]}
        with open("Protocol\\public_key.json", "w") as f:
            json.dump(data,f)
        
    return keys

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
    with Sender(IP, Port) as r:
            with open(path, "rb") as f:
                while m := f.read(1024): r.send(m)

def recieving():
    IP, Port = enterIP()
    key = create_key()
    print(f"server awaiting connection")
    with Receiver(IP, Port, key) as r:
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
    IP, Port = enterIP()
    with Sender(IP, Port) as r:
        while m := input("> "): r.send(m.encode())

def message_recieving():
    IP, Port = enterIP()
    key = create_key()
    print(f"server awaiting connection")
    with Receiver(IP, Port, key) as r:
        print(f"connected")
        while m := r.get_message(): print(m.decode())