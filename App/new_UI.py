import json

from Protocol import file_transfer, Receiver, Sender
from RSA import generate_keys

def secure_file_tranfer():
    while True:
        print(""" 
Welcome to secure file tranfering program.
    1 - Sending File
    2 - Recieving file
    3 - Exit
Press Number You Wanna Do: """)

        match input():
            case "1": sending()
            case "2": recieving()
            case "3": exit(0)
            case _:   print("invalid inputs")

def create_key():
    print("The minimum key size is 256")
    size = int(input("Enter keys size: "))
    if size < 256:
        print("Too small! Try again")
        create_key()
    else:
        keys = generate_keys(size)
        with open("App\config.json", "r") as f:
            config = json.loads(f.read())
        try:
            config["keys"] = keys
        except ValueError:
            print("Invalid input. Please enter a valid value.")
        with open("App\config.json", "w") as f:
            json.dump(config, f, indent=4)  # Write back to file with indentation

def enterIP():
    IP = input("Enter IP:")
    PORT = int(input("Enter Port: "))
    return IP, PORT

def reading_key():
    with open("App\config.json", "r") as f:
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
    create_key()
    key = reading_key()
    print(f"server awaiting connection")
    with Receiver(IP, Port, key) as r:
        print(f"connected")
        with open("Test Files\\random_bytes_receive.bin", "wb") as f:
            while m := r.get_message(): f.write(m)
    print(f"done")
    #conn, addr = file_transfer.await_conn(IP,Port,key)
    #print(f"connected from {addr}")
    #print(f"decrypting...")
    #data = file_transfer.receive_and_decrypt(conn, key)
    #print(f"writing to file")
    #recieve_path = input("Enter recieving path: ")
    #with open(recieve_path, "wb") as f:
    #    f.write(data)
    #print(f"done")