
def encrypt(message: bytes, encrypt_key: tuple[int, int]):
    e, n = encrypt_key
    block_size = (n.bit_length() // 8) - 1
    cipher_block_size = (n.bit_length() // 8) + 1
    cipher_text = []
    for i in range(0, len(message), block_size):
        block = message[i : i + block_size]

        block_int = int.from_bytes(block)
        cipher_int = pow(block_int, e, n)
        cipher_bytes = cipher_int.to_bytes(cipher_int.bit_length() // 8 + 1)
        cipher_bytes = b'\x00' * (cipher_block_size - len(cipher_bytes)) + cipher_bytes
        cipher_text.append(cipher_bytes)
    return b''.join(cipher_text)

def decrypt(cipher_text: bytes, decrypt_key: tuple[int, int]):
    d, n = decrypt_key
    cipher_block_size = (n.bit_length() // 8) + 1
    decrypted_message = []
    for i in range(0, len(cipher_text), cipher_block_size):
        block = cipher_text[i : i + cipher_block_size]
        cipher_int = int.from_bytes(block)
        block_int = pow(cipher_int, d, n)
        block_bytes = block_int.to_bytes(block_int.bit_length() // 8 + 1)
        decrypted_message.append(block_bytes)
    return b''.join(decrypted_message)

if __name__ == "__main__":
    from generate_keys import generate_keys

    message = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in \
        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla \
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in \
        culpa qui officia deserunt mollit anim id est laborum.\
    """.encode()

    pub, priv = generate_keys(512)
    cipher_text = encrypt(message, pub)
    print(cipher_text)
    original_message = decrypt(cipher_text, priv)
    print(original_message)

    


