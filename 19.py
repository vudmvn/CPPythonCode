import sys

sys.stdin = open("inp.txt", "r")

n = int(input())

a = []
for i in range(n):
    t, d = [int(x) for x in input().split()]
    a.append((t, d, t + d))

a.sort(key=lambda x: x[0])

# print(a)

finish = 0
for tpl in a:
    finish = max(finish + tpl[1], tpl[2])

print(finish)
