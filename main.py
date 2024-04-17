from Protocol import chat_tcp, send_data, receive_stream
import RSA

IP = "127.0.0.1"
PORT = 5000

mode = input("enter mode - receive (r), send (s)")
match mode:
    case 'r':
        keys = RSA.generate_keys(512)
        data_stream = receive_stream(IP, PORT, keys) # we only need d and n
        with open("Test Files\\random_bytes_receive.bin", "wb") as f:
            for d in data_stream:
                print(f"writing to file")
                f.write(d)
    case 's':
        with open("Test Files\\random_bytes.bin", "rb") as f:
            send_data(IP, PORT, f.read())
    case _: exit()
