import sys
import itertools

sys.stdin = open("inp.txt", "r")

n = int(input())
a = [int(x) for x in input().split()]

a.sort()

b = itertools.accumulate(a)
