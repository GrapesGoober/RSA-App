from Protocol import Receiver, Sender

IP = "127.0.0.1"
PORT = 5000

mode = input("enter mode - receive (r), send (s)")
match mode:
    # this code here is a chat channel
    case 'r':
        print(f"awaiting connection")
        with Receiver(IP, PORT) as r:
            print(f"connected")
            while m := r.get_message(): print(m.decode())
    case 's':
        with Sender(IP, PORT, 'Ava') as r:
            while m := input("> "): r.send(m.encode())