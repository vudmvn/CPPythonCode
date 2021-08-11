import sys

sys.stdin = open("inp.txt", "r")


def max_subarray(b, m):

    cur_sum = max_rect_local = b[0]

    for i in range(1, m):
        if cur_sum > 0:
            cur_sum += b[i]
        else:
            cur_sum = b[i]

        if cur_sum > max_rect_local:
            max_rect_local = cur_sum

    return max_rect_local


m, n = [int(x) for x in input().split()]

# m, n = map(int, input().split())

a = []
for i in range(m):
    a.append([int(x) for x in input().split()])

# print(a)

sum = [[0 for i in range(n)] for j in range(m)]

for i in range(0, m):
    for j in range(0, n):
        sum[i][j] = a[i][j]
        if j > 0:
            sum[i][j] += sum[i][j - 1]

# print(sum)

max_rect_global = -1e9

for c1 in range(0, n):
    for c2 in range(c1, n):
        b = []
        for r in range(0, m):
            x = sum[r][c2]
            if c1 > 0:
                x -= sum[r][c1 - 1]
            b.append(x)
        max_rect_local = max_subarray(b, m)

        # print(c1, c2, max_rect_local)

        max_rect_global = max(max_rect_local, max_rect_global)

print(max_rect_global)
