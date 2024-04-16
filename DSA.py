import math
import os

# Helper function to find the modular inverse
def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m

        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x = x + m0

    return x

# Helper function for modular exponentiation
def mod_exp(x, y, p):
    res = 1
    x = x % p

    while y > 0:
        if y & 1:
            res = (res * x) % p

        y = y >> 1
        x = (x * x) % p

    return res

# DSA key generation
def generate_keys():
    q_bits = int(input("Enter the desired length of q in bits: "))
    q = generate_prime(q_bits)
    p = 2 * q + 1

    while not is_prime(p):
        p = 2 * q + 1
        q = generate_prime(q_bits)

    h = 2
    while h < p - 1:
        if pow(h, (p - 1) // q, p) == 1:
            break
        h += 1

    x = random_int(1, q - 1)
    y = pow(h, x, p)

    return p, q, h, x, y

# DSA signature generation
def sign(message, q, p, h, x):
    k = random_int(1, q - 1)
    r = pow(h, k, p) % q
    s = (mod_inverse(k, q) * (hash(message) + x * r)) % q

    return r, s

# DSA signature verification
def verify(message, r, s, q, p, h, y):
    if r < 1 or r > q - 1:
        return False

    if s < 1 or s > q - 1:
        return False

    w = mod_inverse(s, q)
    u1 = (hash(message) * w) % q
    u2 = (r * w) % q
    v = ((pow(h, u1, p) * pow(y, u2, p)) % p) % q

    return v == r

# Helper function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Helper function to generate a random prime number
def generate_prime(bits):
    while True:
        p = random_int(2 ** (bits - 1), 2 ** bits)
        if is_prime(p):
            return p

# Helper function to generate a random integer
def random_int(a, b):
    return a + int.from_bytes(os.urandom(8), byteorder='big') % (b - a + 1)

# Example usage
p, q, h, x, y = generate_keys()

message = input("Enter the message: ").encode()
r, s = sign(message, q, p, h, x)

print(f"p: {p}")
print(f"q: {q}")
print(f"h: {h}")
print(f"x (private key): {x}")
print(f"y (public key): {y}")
print(f"r: {r}")
print(f"s: {s}")

verify_message = input("Enter the message to verify: ").encode()

if verify(verify_message, r, s, q, p, h, y):
    print("Signature is valid.")
else:
    print("Signature is invalid.")