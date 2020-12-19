from random import randint


# Given a number n, returns it in binary as a list
# Eg. DecimalToBinaryList(24) returns [1, 1, 0, 0, 0]
# whereas using bin(24) would have returned '0b11000'.
def DecimalToBinaryList(n):
    result = []
    result.append(n % 2)
    while n > 1:
        n = n // 2
        result.append(n % 2)
    result.reverse()
    return result


# Implementation of Modular Exponentiation
# as described on page 79 of textbook
# b^e (mod m)
def ModExp(b, e, m):
    ebinary = DecimalToBinaryList(e)
    result = 1
    if ebinary[-1] != 0:
        result = b
    while len(ebinary) > 1:
        ebinary.pop(-1)
        b = (b**2) % m
        if ebinary[-1] == 1:
            result *= b
            result %= m
    return result


# Returns a randomly generated decimal integer of length n.
def RandIntLength(n):
    return randint(10**(n-1), (10**n)-1)


# Fermat's Primality Test:
# Given an integer n, a number to test for primality,
# and an integer k, the number of rounds of testing,
# returns true if n is prime, and false otherwise.
def IsPrime(n, k):
    if n % 2 == 0:
        if n == 2:
            return True
        return False
    for _ in range(k):
        r = randint(2, n - 2)
        r = ModExp(r, n-1, n)
        if r != 1:
            return False
    return True


# Generates a random prime number of length n
def GetPrime(n):
    p = RandIntLength(n)
    while not IsPrime(p, 100):
        p = RandIntLength(n)
    return p


# Extended Euclidean Algorithm,
# used for finding a modular inverse
# gcd(a, b) = ax + by
# Returns [gcd(a, b), x, y]
def EEA(a, b):
    if a == 0:
        g = b
        x = 0
        y = 1
    else:
        eea = EEA(b % a, a)
        g = eea[0]
        x = eea[2] - (b//a) * eea[1]
        y = eea[1]
    return (g, x, y)


# returns a^-1 (mod b)
def EEAInv(a, b):
    return EEA(a, b)[1] % b
