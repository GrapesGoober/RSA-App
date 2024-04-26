from Protocol import file_transfer, Receiver, Sender
import RSA

IP = "127.0.0.1"
PORT = 5000

mode = input("enter mode - receive (r), send (s)")
match mode:
    case 'r':
        print(f"generating keys")
        keys = RSA.generate_keys(512)
        print(f"server awaiting connection")
        with Receiver(IP, PORT, keys) as r:
            print(f"connected")
            while m := r.get_message(): print(m.decode())

    case 's':
        with Sender(IP, PORT) as r:
            while m := input("> "): r.send(m.encode())
    case _: exit()
