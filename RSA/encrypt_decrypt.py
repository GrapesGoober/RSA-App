from typing import Generator

def get_block_size(n: int):
    block_size = (n.bit_length() - 1) // 8
    cipher_block_size = block_size + 1
    return block_size, cipher_block_size

def get_blocks(message: bytes, size_bytes: int) -> Generator[int, None, None]:
    for pos in range(0, len(message), size_bytes):
        block = message[pos:pos + size_bytes]
        yield block

def get_padded_blocks(message: bytes, block_size: int):
    for block in get_blocks(message, block_size):
        padding = block_size - len(block)
        if padding > 0: block += b'1' + b'0' * (padding - 1)
        yield block

    if len(message) % block_size == 0: # add an artificial padding
        yield b'1' + b'0' * (block_size - 1)

def encrypt_blocks(message: bytes, modulo: int, expo: int = 65537):
    block_size, cipher_block_size = get_block_size(modulo)
    for block in get_padded_blocks(message, block_size):
        block = int.from_bytes(block)
        c = pow(block, expo, modulo)
        yield c.to_bytes(cipher_block_size)

def decrypt_blocks(message: bytes, key: tuple[int, int]):
    k_decrypt, modulo = key
    block_size, cipher_block_size = get_block_size(modulo)
    for block in get_blocks(message, cipher_block_size):
        block = int.from_bytes(block)
        c = pow(block, k_decrypt, modulo)
        yield c.to_bytes(block_size)

def encrypt(message: bytes, modulo: int, expo: int = 65537):
    return b"".join(encrypt_blocks(message, modulo, expo=expo))

def decrypt(message: bytes, key: tuple[int, int]):
    plain_text = b"".join(decrypt_blocks(message, key))
    return plain_text.rsplit(b'1', 1)[0]

