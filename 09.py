import sys

sys.stdin = open("inp.txt", "r")

n = int(input())
a = []
while True:
    try:
        a.extend([int(x) for x in input().split()])
        # break
    except EOFError:
        break

inversion = []

for i in range(n):
    inversion_at_i = 0
    for j in range(i):
        if a[j] > a[i]:
            inversion_at_i += 1
    inversion.append(inversion_at_i)

for x in inversion:
    print(x, end=" ")
