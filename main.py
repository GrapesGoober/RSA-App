from Protocol import file_transfer
import RSA

IP = "127.0.0.1"
PORT = 5000

mode = input("enter mode - receive (r), send (s)")
match mode:
    case 'r':
        print(f"generating keys")
        keys = RSA.generate_keys(1024)
        print(f"setting server")
        conn, addr = file_transfer.await_conn(IP, PORT, keys)
        print(f"connected from {addr}")
        print(f"decrypting...")
        data = file_transfer.receive_and_decrypt(conn, keys)
        print(f"writing to file")
        with open("Test Files\\random_bytes_receive.bin", "wb") as f:
            f.write(data)
        print(f"done")

    case 's':
        with open("Test Files\\random_bytes.bin", "rb") as f:
            file_transfer.send_data(IP, PORT, f.read())
    case _: exit()
