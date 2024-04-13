from Protocol import chat_tcp, send_stream, receive_stream
import RSA

IP = "127.0.0.1"
PORT = 5000

mode = input("enter mode - receive (r), send (s)")
match mode:
    case 'r':
        k_pub, k_priv = RSA.generate_keys(512)
        receive_stream(IP, PORT, k_pub[1])
    case 's':
        send_stream(IP, PORT, None)
    case _: exit()
