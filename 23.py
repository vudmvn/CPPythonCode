import sys

sys.stdin = open("inp.txt", "r")

n = int(input())

a = [int(x) for x in input().split()]

cnt = 0
pair = []
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            cnt += 1
            pair.append((i + 1, j + 1))

print(cnt)

for p in pair:
    print(p[0], p[1])
