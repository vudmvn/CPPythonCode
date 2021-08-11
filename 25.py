import sys

sys.stdin = open("inp.txt", "r")


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


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
