def sub(str, output=""):
  if len(str) == 0:
    print(output)
    return

  for i in range(len(str)):
    x = str[i+1:] + str[:i] 
    res = str[i].join(x)
    print(res)


  



def permutation(s):
  sub(list(s))

print(permutation("ABC"))
