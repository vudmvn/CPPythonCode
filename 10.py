import sys

sys.stdin = open("inp.txt", "r")

n = int(input())
inversion = []
while True:
    try:
        inversion.extend([int(x) for x in input().split()])
        # break
    except EOFError:
        break

a = [-1 for i in range(n)]
mark = [False for i in range(n)]

# observation: the largest element is the last element with 0 inversions
# how to use this observation to find original sequences from inversions

for i in range(n, 0, -1):
    for j in range(n - 1, -1, -1):
        if inversion[j] == 0 and mark[j] == False:

            # the next largest element
            a[j] = i
            mark[j] = True

            # reduce the number of inversions for elements after the index j
            for k in range(j + 1, n):
                if mark[k] == False:
                    inversion[k] -= 1

            break

for x in a:
    print(x, end=" ")
