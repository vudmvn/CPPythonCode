import sys

sys.stdin = open("inp.txt", "r")


def nbbit(n):
    return len(bin(n)[2:])


# observation: we try to answer the following question - how we can obtain the value of a_n
# the only rule we have is the rule given by the problem.
# assume that 2^k + 1 <= n <= 2^{k+1}; so all elements a_{2^k+1} .. a_{2^{k+1}} are generated from elements a_1 .. a_{2^k}
# so a_n is equal to (a_m + 1)%3 where m=n-2^k
# if m !=0, we repeat this step for m until we reach the base case


def digit(n):
    cnt = 0
    while n > 1:
        number_of_bit = nbbit(n)
        # print(n, number_of_bit)
        if n > (1 << (number_of_bit - 1)):
            n -= 1 << (
                number_of_bit - 1
            )  # regular case: 2^{k}+1 <= n < 2^{k+1} - n has k+1 bits
        else:
            n -= 1 << (number_of_bit - 2)  # special case: = 2^{k+1} - n has k+2 bit
        cnt += 1
    return cnt % 3


while True:
    try:
        n = int(input())
        print(digit(n))
    except EOFError:
        break
