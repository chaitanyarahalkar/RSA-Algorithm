from random import randrange,randint

# probabilistic primality tester 
def miller_rabin(n, k):
	if n == 2:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True

# Multiplicative Inverse Calculation 
def mod_inverse(a,m):
	a = a % m
	for i in range(1,m):
		if (a*i) % m == 1:
			return i
	return 1


# RSA Public Private Key Pair Generation 
while True:
	p = randint(1,500)
	q = randint(1,500)
	if miller_rabin(p,64) and miller_rabin(q,64):
		tot = (p-1)*(q-1) # Euler's Totient function 
		n = p*q # modulus 
		break

while True:
	e = randint(3,tot-1) # public key 
	if miller_rabin(e,64):
		break 

priv_key = mod_inverse(e,tot) # private key 


# Encryption and Decryption functions 

# n is the modulus | e is the public key
def encrypt(n,e,data):
	return (data ** e) % n

# enc is the encrypted text | priv_key is the private key
def decrypt(n,priv_key,enc):
	return (enc ** priv_key) % n
