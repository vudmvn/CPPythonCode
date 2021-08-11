n = int(input())
xx = []
yy = []

for i in range(n):
    x, y = input().split()
    xx.append(int(x))
    yy.append(int(y))
    # print(xx)
    # print(yy)

global_min_dis = 1e9
best_index = -1
for i in range(n):
    dis_from_i = 0.0
    for j in range(n):
        dis_from_i += ((xx[i] - xx[j]) ** 2 + (yy[i] - yy[j]) ** 2) ** 0.5
    if dis_from_i < global_min_dis:
        global_min_dis = dis_from_i
        best_index = i

print("%d %.3f" % (best_index + 1, global_min_dis))
