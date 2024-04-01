import random

# Miller-Rabin primality test using 20 iterations
def is_probably_prime(n, iter = 20) -> bool:
	randnum = random.randint(2, n - 2)
	x = pow(randnum, (n - 1) >> 1, n)
	if x == 1 or x == n - 1:
		return True
	for _ in range(iter - 1):
		x = pow(x, 2, n)
		if x == n - 1:
			return True
	return False

# generates 2 prime numbers, p & q
def generate_prime_number() -> int:

	# key size should be sufficiently large
	min_range, max_range = 2**1024, 2**2048

	# keep randomly guessing an odd number until it is prime
	num = random.randint(min_range, max_range) | 1
	while not is_probably_prime(num):
		num += 2
	return num
    
print(generate_prime_number())