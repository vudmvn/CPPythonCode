import sys

sys.stdin = open("inp.txt", "r")

n = int(input())
a = []

for i in range(n):
    x, y = [int(x) for x in input().split()]
    a.append(y)

a.sort()

i, j = 0, n - 1

min_total_distance = 0

while i < j:
    min_total_distance += a[j] - a[i]
    i += 1
    j -= 1

print(min_total_distance)
