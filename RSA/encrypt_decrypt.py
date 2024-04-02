
def encrypt(message: bytes, encrypt_key: tuple[int, int]):
    e, n = encrypt_key
    return pow(message, e, n)

def decrypt(message: bytes, decrypt_key: tuple[int, int]):
    d, n = decrypt_key
    return pow(message, d, n)

if __name__ == "__main__":
    from generate_keys import generate_keys

    message = "hello, can you read this?"
    message_int = int.from_bytes(message.encode())

    pub, priv = generate_keys()
    c = encrypt(message_int, pub)
    m = decrypt(c, priv)

    print(m.to_bytes(30).decode())
    


