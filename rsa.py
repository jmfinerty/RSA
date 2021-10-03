from numbers import GetPrime, EEA, EEAInv, ModExp


# generates public and private keys,
# exports them to files "public_key" and "private_key"
def MakeKeys():
    p = GetPrime(100)
    q = GetPrime(100)
    e = 65537
    gcd = EEA(e, (p-1)*(q-1))[0]
    while ((p - q) < 10**95) or (gcd != 1):
        p = GetPrime(100)
        q = GetPrime(100)
        gcd = EEA(e, (p-1)*(q-1))[0]
    n = p * q
    private = EEAInv(e, (p-1)*(q-1))

    open("public_key", 'w').write(str(n) + '\n' + str(e))
    open("private_key", 'w').write(str(private))


# encrypts "message" file using "public_key" file,
# exports results to "ciphertext"
def EncryptMessage():
    msg = int(open("message", 'r').read())
    n, e = open("public_key", 'r').readlines()
    n = int(n); e = int(e)
    ciphertext = ModExp(msg, e, n)
    open("ciphertext", 'w').write(str(ciphertext))


# encrypts "ciphertext" file using "private_key" file,
# exports results to "decrypted_message"
def DecryptMessage():
    ciphertext = int(open("ciphertext", 'r').read())
    n = int(open("public_key", 'r').readline())
    d = int(open("private_key", 'r').read())
    msg = ModExp(ciphertext, d, n)
    open("decrypted_message", 'w').write(str(msg))
