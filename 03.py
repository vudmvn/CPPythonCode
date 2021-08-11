from _typeshed import StrPath, SupportsLenAndGetItem
import sys

sys.stdin = open("inp.txt", "r")

n = int(input())
x, y = [], []

for i in range(n):
    xx, yy = [int(x) for x in input().split()]
    x.append(xx)
    y.append(yy)

min_diameter = 1e9

for i in range(n):
    for j in range(n):
        if i == j:
            continue
