#https://codeforces.com/group/SQsuqIyFPU/contest/335250/problem/02

import collections

n = int(input())
arr = []

while True:
    try:
        line=input()
        tmpArr = [int(x) for x in line.split()]
        
        # arr += tmpArr
        
        arr.extend(tmpArr)

        # for x in tmpArr:
        #     arr.append(x)
        # print(arr)
    except EOFError:
        break
    


freq = {} #a dictionary

for x in arr:
    freq[x] = 0

for x in arr:
    freq[x] += 1

 
print(len(freq))

for k in sorted(freq):
    print (k,freq[k])