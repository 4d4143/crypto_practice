# CryptoMath module
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)


# greatest common denominator function

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None

    # We now use the extended Euclidean algorithm to calculate the mod inverse
    # Added a print to see the iteration and how the algorithm works

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    i = 1
    while v3 != 0:

        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q*v1), (u2 - q*v2), (u3 - q*v3)\
            , v1, v2, v3

    return u1 % m
