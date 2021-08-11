import sys

sys.stdin = open("inp.txt", "r")

s = str(input())
K = int(input())

# print(s)
# print(K)

pos = 0

while K > 0 and pos + 1 < len(s):
    # print(K, pos, s)
    if s[pos] > s[pos + 1]:
        s = s[:pos] + s[pos + 1 :]
        K -= 1
        if pos > 0:
            pos -= 1
    else:
        pos += 1

# print(K, s)
print(s if K == 0 else s[:-K])
