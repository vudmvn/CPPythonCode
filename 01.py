# https://codeforces.com/group/SQsuqIyFPU/contest/335250/problem/02

n = int(input())
arr = []

while True:
    try:
        line = input()
        tmpArr = [int(x) for x in line.split()]

        arr += tmpArr  # cách 1

        # arr.extend(tmpArr) # cách 2

        # for x in tmpArr:   #cách 3
        #     arr.append(x)

        # print(arr)
    except EOFError:
        break

min_ave = 1e9
max_ave = -1e9

for i in range(0, n - 1):
    sum = arr[i]
    for j in range(i + 1, n):
        sum += arr[j]
        if min_ave * (j - i + 1) > sum:
            min_ave = sum / (j - i + 1)
        if max_ave * (j - i + 1) < sum:
            max_ave = sum / (j - i + 1)

print("%.3f %.3f" % (min_ave, max_ave))
