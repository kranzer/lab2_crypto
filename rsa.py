from utils import get_inversed


def generate_key_pair(p, q):
    n = p * q
    e = 65537

    phi = (p - 1) * (q - 1)
    d = get_inversed(e, phi)

    return {"modulo": n, "exponent": e, "secret": d}


def encrypt(M, n, e):
    return pow(M, e, n)


def decrypt(C, n, d):
    return pow(C, d, n)


def sign(M, n, d):
    S = pow(M, d, n)
    return (M, S)


def verify(M, S, n, e):
    return M == pow(S, e, n)


def send_key(k, e1, n1, n, d):
    k1 = encrypt(k, n1, e1)
    S = sign(k, n, d)
    S1 = encrypt(S[1], n1, e1)
    return (k1, S1)


def receive_key(k1, S1, d, n, e1, n1):
    k = decrypt(k1, n, d)
    print(k)
    S = decrypt(S1, n, d)
    print(S)
    return (k, verify(k, S, n1, e1))