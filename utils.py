import random
from math import gcd

from generator import BBSBytes

def miller_rabin(n, k):
    n = int(n)
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    d = (n-1)//pow(2,s)
    for i in range(0, k):
        x = random.randint(2, n)
        if gcd(x, n) == 1:
            if pow(x, d, n) == 1 or pow(x,d,n) == n-1:
                continue
            else:
                steps = 0
                for r in range(1, s):
                    # print(r)
                    power = d*(pow(2, r))
                    x_r = pow(x, power, n)
                    if x_r == n-1:
                        break
                    steps = r
                if steps == s-1:
                    return False
            # if strong:
            #     if i+1 < k:
            #         i += 1
            #         continue
            #     else:
            #         return True
            # else:
            #     return False

        else:
            return False
    return True

def generate_p_q(bits=256):
    b = BBSBytes(bits)
    p = 0
    q = 0
    while True:
        temp = b.generate_random()
        temp |= (1 << bits)
        temp |= 1
        if miller_rabin(temp, 10):
            p = temp
            break

    while True:
        temp = b.generate_random()
        temp |= (1 << bits)
        if miller_rabin(temp, 10):
            q = temp
            break
    return p, q


def extended_gcd(a, m):
    if a == 0:
        return (m, 0, 1)
    else:
        gcd_, v, u = extended_gcd(m % a, a)
        return gcd_, u - (m // a) * v, v


def get_inversed(a, m):
    gcd_, u, v = extended_gcd(a, m)
    if gcd_ != 1:
        raise Exception('no inverse element')
    else:
        return u % m

