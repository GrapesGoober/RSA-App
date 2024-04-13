from Protocol import chat_tcp, send_data, receive_stream
import RSA

IP = "127.0.0.1"
PORT = 5000

mode = input("enter mode - receive (r), send (s)")
match mode:
    case 'r':
        k_pub, k_priv = RSA.generate_keys(512)
        data_stream = receive_stream(IP, PORT, k_priv) # we only need d and n
        with open("Test Files\\receiving_file.txt", "wb") as f:
            for d in data_stream:
                f.write(d)
    case 's':
        with open("Test Files\\sending_file.txt", "rb") as f:
            send_data(IP, PORT, f.read())
    case _: exit()
