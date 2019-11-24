# Maximum occured element
def maxOccured(left,right,n,maxx):
    
      arr = [0 for i in range(maxx+1)]
      for i in range(n):
        x = left[i]
        arr[x] += 1
      
      add = 0
      for i in range(maxx+1):
        add += arr[i]
        arr[i] = add
     
      for j in range(n):
        y = right[j]
        arr[y] -= 1
     
      return max(arr)
      
T = int(input())
for _ in range(T):
  n = int(input())
  left = [int(x) for x in input().split()]
  right = [int(x) for x in input().split()]
  m = max(right)

  print(maxOccured(left,right,n,m)) 
