import sys

sys.stdin = open("inp.txt", "r")

n, K = [int(x) for x in input().split()]
arrival = [int(x) for x in input().split()]

arrival.sort()
