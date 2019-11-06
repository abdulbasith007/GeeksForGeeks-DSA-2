import math

for x in range(int(input())):
    n = int(input())
    if n == 0:
        print(0)
    else:
        print(int(math.log2(n&-n)+1))


# Remember the following while doing Bit Manipulation problems:

# log2(n & -n)+1 - > returns the position of the rightmost set bit
# log2(n)+1 -> returns the number of digits in the binary representation of the given number
# log10(n)+1 -> returns the number of digits in the number decimal number O(1) time
# x=x&(x-1) -> turn off the rightmost set bit
# 1<<n --=""> 1*(2^n) and all the term will be zero except the one