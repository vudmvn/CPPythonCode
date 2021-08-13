import sys

sys.stdin = open("inp.txt", "r")


def cmp(a, b):
    return a + b < b + a


n = int(input())
a = []
while True:
    try:
        a.extend([str(x) for x in input().split()])
        # break
    except EOFError:
        break

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] < a[j] + a[i]:
            a[i], a[j] = a[j], a[i]

for x in a:
    print(x, end="")
