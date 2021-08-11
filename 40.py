import sys

sys.stdin = open("inp.txt", "r")


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n = int(input())
a = [int(x) for x in input().split()]

max_length = 0
for i in range(n):
    d = a[i]
    for j in range(j + 1, n):
        d = gcd(d, a[j])
        if d > 1:
            max_length = max(max_length, j - i + 1)
        else:
            break

print(max_length)
