import random

SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 
	61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 
	149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 
	229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

# Miller-Rabin primality test using 15 iterations
def is_probably_prime(n, iter = 15) -> bool:

	# simple small primes primality check first, to catch easy cases
	for i in SMALL_PRIMES:
		if n % i == 0:
			return False

	r, s = 0, n - 1
	while s % 2 == 0:
		r += 1
		s //= 2
	for _ in range(iter):
		a = random.randrange(2, n - 1)
		x = pow(a, s, n)
		if x == 1 or x == n - 1: continue
		for _ in range(r - 1):
			x = pow(x, 2, n)
			if x == n - 1: break
		else: return False
	return True

# generates a random prime number
def generate_prime(size: int = 1024) -> int:

	# key size should be sufficiently large
	min_range, max_range = 2**size, 2**(size * 2)

	# keep randomly guessing an odd number until it is prime
	num = random.randint(min_range, max_range) | 1
	while not is_probably_prime(num):
		num += 2
	return num

# generate RSA keys, returns public key and private key
def generate_keys(size: int = 1024) -> tuple[tuple[int, int], tuple[int, int]]:
    p = generate_prime(size)
    q = generate_prime(size)
    n = p * q
    z = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, z)
    return (e, n), (d, n)

