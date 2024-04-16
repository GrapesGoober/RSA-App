# This code is to generate a large test file full of random bytes
import random

iterations = 1000
size = 1024
with open("Test Files\\random_bytes.bin", "wb") as f:
    for _ in range(iterations):
        randnum = random.randint(0, 2 ** (size * 8))
        f.write(randnum.to_bytes(size))