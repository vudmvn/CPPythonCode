import sys

sys.stdin = open("inp.txt", "r")

sz = 201
n = int(input())

a = [[0 for j in range(sz)] for i in range(sz)]

for i in range(n):
    x, y, z, t = [int(w) + 100 for w in input().split()]

    for p in range(x, z):
        for q in range(y, t):
            a[p][q] = 1

# print(a)

cover = 0
for i in range(sz):
    for j in range(sz):
        cover += a[i][j]

print(cover)
