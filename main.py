from Protocol import chat_tcp, send_data, receive_data
import RSA

IP = "127.0.0.1"
PORT = 5000

mode = input("enter mode - receive (r), send (s)")
match mode:
    case 'r':
        print(f"generating keys")
        keys = RSA.generate_keys(1024)
        print(f"setting server")
        data = receive_data(IP, PORT, keys) # we only need d and n
        with open("Test Files\\random_bytes_receive.bin", "wb") as f:
            print(f"writing to file")
            f.write(data)
    case 's':
        with open("Test Files\\random_bytes.bin", "rb") as f:
            send_data(IP, PORT, f.read())
    case _: exit()
