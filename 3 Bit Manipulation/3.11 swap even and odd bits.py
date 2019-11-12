# Logic: 
# 1) Do AND with (10101010) to get the positions of the even set bits (res1)  
# 2) Do AND with (01010101) to get the positions of the odd set bits (res2)
# 3) Now, do >>1 for the first result and perform <<1 for 2nd result
# 4) Finally, return the OR of both the results

def swapBits(n):
  res1 = n & 0xAAAA
  res2 = n & 0x555555
  
  res1 >>= 1
  res2 <<= 1
  
  return res1 | res2

print(swapBits(23)) 




