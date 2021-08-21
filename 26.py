import sys

sys.stdin = open("E:\\inp.txt", "r")

n = int(input())
xau_bi = input()
so_bi = [0]*3

for bi in xau_bi:
    if bi == 'T':
        so_bi[1]+=1
    elif bi == 'X':
        so_bi[0]+=1
    else:
        so_bi[2]+=1


so_bi_trong_tung_vung = [[0 for _ in range(3)] for _ in range(3)]

for bi in xau_bi:
    

