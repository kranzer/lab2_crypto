from utils import generate_p_q
from rsa import *


def main():
    while True:
        p, q = generate_p_q()
        p1, q1 = generate_p_q()
        if p*q < p1*q1:
            break

    message = 10000
    user_a = generate_key_pair(p, q)
    user_b = generate_key_pair(p1, q1)
    encrypted = encrypt(message, user_a['modulo'], user_a['exponent'])
    print(user_a['modulo'])
    print(user_a['exponent'])
    print(encrypted)
    decrypted = decrypt(encrypted, user_a['modulo'], user_a['secret'])
    print(decrypted)


    message = 12414123421
    signed = sign(message, user_a['modulo'], user_a['secret'])
    print(verify(signed[0], signed[1], user_a['modulo'], user_a['exponent']))

    print('user_a key')
    key = send_key(message, user_b['exponent'], user_b['modulo'], user_a['modulo'], user_a['secret'])
    print('user_b key')
    print(receive_key(key[0], key[1], user_b['secret'], user_b['modulo'], user_a['exponent'], user_a['modulo']))


if __name__ == '__main__':
    main()