import sys

sys.stdin = open("inp.txt", "r")

m, n = [int(x) for x in input().split()]

a = []

for i in range(m):
    a.append([int(x) for x in input().split()])


visiable = [[False for j in range(n)] for i in range(m)]

# max_height = a.copy() #wrong - address assignment

max_height = [[a[i][j] for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        if j > 0:
            max_height[i][j] = max(max_height[i][j - 1], a[i][j])
        if max_height[i][j] == a[i][j]:
            visiable[i][j] = True

max_height = [[a[i][j] for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n - 1, -1, -1):
        if j < n - 1:
            max_height[i][j] = max(max_height[i][j + 1], a[i][j])
        if max_height[i][j] == a[i][j]:
            visiable[i][j] = True


max_height = [[a[i][j] for j in range(n)] for i in range(m)]

for j in range(n):
    for i in range(m):
        if i > 0:
            max_height[i][j] = max(max_height[i - 1][j], a[i][j])
        if max_height[i][j] == a[i][j]:
            visiable[i][j] = True


max_height = [[a[i][j] for j in range(n)] for i in range(m)]


for j in range(n):
    for i in range(m - 1, -1, -1):
        if i < m - 1:
            max_height[i][j] = max(max_height[i + 1][j], a[i][j])
        if max_height[i][j] == a[i][j]:
            visiable[i][j] = True

ret = 0
for i in range(m):
    for j in range(n):
        if visiable[i][j] == True:
            ret += 1


print(ret)
