from App import secure_file_tranfer
from Protocol import file_transfer, Receiver, Sender
import RSA

IP = "127.0.0.1"
PORT = 5000

#mode = input("enter mode - receive (r), send (s)")
#match mode:
    # # this code here is a chat channel
    # case 'r':
    #     print(f"generating keys")
    #     keys = RSA.generate_keys(512)
    #     print(f"server awaiting connection")
    #     with Receiver(IP, PORT, keys) as r:
    #         print(f"connected")
    #         while m := r.get_message(): print(m.decode())
    # case 's':
    #     with Sender(IP, PORT) as r:
    #         while m := input("> "): r.send(m.encode())

    
    # this code here is a file sending channel
#    case 'r':
#        print(f"generating keys")
#        keys = RSA.generate_keys(512)
#        print(f"server awaiting connection")
#        with Receiver(IP, PORT, keys) as r:
#            print(f"connected")
#            with open("Test Files\\random_bytes_receive.bin", "wb") as f:
#               while m := r.get_message(): f.write(m)
#        print(f"done")
#    case 's':
#        with Sender(IP, PORT) as r:
#            with open("Test Files\\random_bytes.bin", "rb") as f:
#                while m := f.read(1024): r.send(m)
#    case _: exit()
secure_file_tranfer()