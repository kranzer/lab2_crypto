import random


class BBSBytes:
    p = 0xD5BBB96D30086EC484EBA3D7F9CAEB07
    q = 0x425D2B9BFDB25B9CF6C416CC6E37B59C1F

    n = p * q

    def __init__(self, iterations=10):
        self.iterations = iterations

    def generate_random(self):
        r = random.randint(2, self.n)
        x = []

        for i in range(0, self.iterations):
            r = pow(r, 2, self.n)
            x.append(r % 2)

        result = 0
        for bit in x:
            result = (result << 1) | bit
        return result
