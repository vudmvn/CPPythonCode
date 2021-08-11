n = int(input())
arr = []

while True:
    try:
        arr.extend([int(x) for x in input().split()])
        #break
    except EOFError:
        break

arr.extend(arr)

min_sum = arr[0]

for i in range(n - 1, 2 * n):
    sum = 0
    for j in range(i, i - n + 1, -1):
        sum += arr[j]
        if sum < min_sum:
            min_sum = sum

print(min_sum)
