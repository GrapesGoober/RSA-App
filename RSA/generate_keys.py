from generate_prime import generate_prime

# generate RSA keys, returns (K+, K-)
def generate_keys() -> tuple[int, int, int]:
    p = generate_prime()
    q = generate_prime()
    n = p * q
    z = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, z)
    return (e, n), (d, n)

