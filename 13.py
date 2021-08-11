import sys

sys.stdin = open("inp.txt", "r")

n = int(input())
s = str(input())

x, y = 0, 0

for c in s:
    if c == "G":
        y += 1
    if c == "L":
        x -= 1
    if c == "R":
        x += 1
    if c == "B":
        y -= 1

print(x, y)
