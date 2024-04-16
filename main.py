from RSA import generate_keys, encrypt, decrypt
import random

def generate_large_message(size: int = 300) -> bytes:
    message_list = []
    for _ in range(size):
        randint = random.randrange(0, 2 ** 8)
        randbytes = randint.to_bytes(length=1)
        message_list.append(randbytes)
    return b"".join(message_list)

message = generate_large_message()
pub, priv = generate_keys(512)
cipher_text = encrypt(message, pub)
decrypted = decrypt(cipher_text, priv)
print(decrypted == message)