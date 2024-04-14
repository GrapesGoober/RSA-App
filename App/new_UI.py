import json

from Protocol import send_data, receive_stream
from RSA import generate_keys

def secure_file_tranfer():
    while True:
        print(""" 
Welcome to secure file tranfering program.
    1 - Sending File
    2 - Reading a recieve file
    3 - Exit
Press Number You Wanna Do: """)

        match input():
            case "1": sending()
            case "2": recieving()
            case "3": exit(0)
            case _:   print("invalid inputs")

def generate_keys():
    print("The minimum key size is 256")
    size = int(input("Enter keys size: "))
    if size < 256:
        print("Too small! Try again")
        generate_keys()
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

def sending():
    generate_keys()
    dest_IP = input("Enter IP: ")
    dest_PORT = int(input("Enter Port: "))
    data = ""
    send_data(dest_IP,dest_PORT,data)

def recieving():
    dest_IP = input("Enter IP: ")
    dest_PORT = int(input("Enter Port: "))
    key = []
    receive_stream(dest_IP,dest_PORT,key)