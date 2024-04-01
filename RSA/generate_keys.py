import random

# Miller-Rabin primality test using 15 iterations
def is_probably_prime(n, iter = 15) -> bool:
	# simple small factor primality check first, to catch easy cases
	for i in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
		if n % i == 0:
			return False
	# run the Miller-Rabin algorithm
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