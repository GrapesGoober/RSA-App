from RSA import generate_keys, encrypt, decrypt, get_block_size
import random

def generate_large_message(size: int = 300) -> bytes:
    message_list = []
    for _ in range(size):
        randint = random.randrange(0, 2 ** 8)
        randbytes = randint.to_bytes(length=1)
        message_list.append(randbytes)
    return b"".join(message_list)
    

d, n = generate_keys(512)
for size in range(300, 6000, 100):
    message = generate_large_message(size)
    cipher_text = encrypt(message, n)
    decrypted = decrypt(cipher_text, (d, n))
    if (decrypted != message):
        blocksize, _ = get_block_size(n)
        print("failed", len(message) % blocksize)