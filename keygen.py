import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = y2 - temp1 * y1

        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if temp_phi == 1:
        d = y2

    return d % phi

def KeyGen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = multiplicative_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def RSA(message, key):
    result = []
    key, n = key

    for char in message:
        # RSA encryption/decryption formula: c = (m^key) % n
        m = ord(char)
        c = pow(m, key, n)
        result.append(c)

    return result

def RSA_decrypt(ciphertext, key):
    result = []
    key, n = key

    for c in ciphertext:
        # RSA decryption formula: m = (c^key) % n
        m = pow(c, key, n)
        result.append(chr(m))

    return "".join(result)

# Example usage
public_key, private_key = KeyGen(53, 59)
message = "hello"
encrypted = RSA(message, public_key)
decrypted = RSA_decrypt(encrypted, private_key)

print("Original message:", message)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)

#Example 2

# Generate the public and private keys
public_key, private_key = KeyGen(17, 23)

# Encrypt a message using the public key
message = "Coding is awesome!"
encrypted = RSA(message, public_key)

# Decrypt the ciphertext using the private key
decrypted = RSA_decrypt(encrypted, private_key)

# Print the results
print("Original message:", message)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
