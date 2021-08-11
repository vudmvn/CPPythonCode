import sys

# sys.stdin = open("inp.txt", "r")

n, K = int(input()), int(input())

cx, cy = (n + 1) // 2, (n + 1) // 2

min_energy = 0
for k in range(K):
    x, y = [int(x) for x in input().split()]
    h = abs(x - cx)
    w = abs(y - cy)
    if h < w:
        h, w = w, h
    min_energy += 5 * w + 10 * h

print(min_energy)
