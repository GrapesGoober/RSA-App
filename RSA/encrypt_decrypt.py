from typing import Generator

def get_block_size(n: int):
    block_size = (n.bit_length() - 1) // 8
    cipher_block_size = block_size + 1
    return block_size, cipher_block_size

def get_blocks(message: bytes, size_bytes: int) -> Generator[int, None, None]:
    for pos in range(0, len(message), size_bytes):
        block = message[pos:pos + size_bytes]
        yield int.from_bytes(block)

def encrypt(message: bytes, modulo: int, expo: int = 65537):
    block_size, cipher_block_size = get_block_size(modulo)
    cipher_text = []

    padding = len(message) % block_size
    if padding > 0: message += b'1' + b'\0' * (padding - 1)
    if padding == 0: message += b'1' + b'\0' * (block_size - 1)
        
    for block in get_blocks(message, block_size):
        c = pow(block, expo, modulo)
        cipher_text.append(c.to_bytes(cipher_block_size))
    return b''.join(cipher_text)

def decrypt(message: bytes, key: tuple[int, int]):
    k_decrypt, modulo = key
    block_size, cipher_block_size = get_block_size(modulo)
    message_text = []
    for block in get_blocks(message, cipher_block_size):
        c = pow(block, k_decrypt, modulo)
        message_text.append(c.to_bytes(block_size))
    return b"".join(message_text).rsplit(b'1', 1)[0]

