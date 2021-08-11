# https://www.geeksforgeeks.org/python-prefix-sum-list/

import sys

from itertools import accumulate

# sys.stdin = open("inp.txt", "r")


def check_if_divisable(k, acc_sum, sum):
    # print(k, acc_sum, sum)
    pos = -1
    for i in range(1, k):
        try:
            pos = list(acc_sum).index(sum * i, pos + 1)
            # print(i, pos)
        except ValueError:
            return False
    return True


n = int(input())
a = []

while True:
    try:
        a.extend([int(x) for x in input().split()])
        # break
    except EOFError:
        break

acc_sum = list(accumulate(a))

# print(acc_sum)

divisable = False

for k in range(n, 1, -1):
    if acc_sum[n - 1] % k != 0:
        continue

    if check_if_divisable(k, acc_sum, acc_sum[n - 1] // k) == True:
        print(k)
        divisable = True
        break

if divisable == False:
    print(1)
