from RSA import generate_keys, encrypt, decrypt

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