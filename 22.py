import sys
import math

sys.stdin = open("inp.txt", "r")


def nbbit(n):
    return len(bin(n)[2:])


def digit(n):
    cnt = 0
    while n > 1:
        number_of_bit = nbbit(n)
        # print(n, number_of_bit)
        if n > (1 << (number_of_bit - 1)):
            n -= 1 << (number_of_bit - 1)
        else:
            n -= 1 << (number_of_bit - 2)
        cnt += 1
    return cnt % 3


while True:
    try:
        n = int(input())
        print(digit(n))
    except EOFError:
        break
