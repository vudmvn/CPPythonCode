import sys

sys.stdin = open("inp.txt", "r")


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


# n / lcm(p,q) : chia het cho p va q (chia het cho ca 2)

# n / p + n / q - n/lcm(p,q): chia het cho p hoac q nhung ko chia het cho ca 2

# n chia het cho ca p , q <=> n chia het cho bscnn (p,q) hay n // lcm(p,q)

# n ko chia het cho r

# n // lcm(p,q) - n //lcm(r,lcm(p,q))

while True:
    try:
        n, p, q, r = [int(x) for x in input().split()]

        w = lcm(lcm(p, q), r)

        ret = int(
            n // lcm(p, q) - n // w + n // lcm(p, r) - n // w + n // lcm(q, r) - n // w
        )

        print(ret)
    except EOFError:
        break
