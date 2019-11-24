# Maximum occured element

def maxOccured(L,R,n,maxx):
    maxx += 5
    arr = [0 for i in range(maxx)] 
     
    for i in range(0, n, 1): 
        arr[L[i]] += 1
        arr[R[i] + 1] -= 1
  
    # Finding prefix sum and index 
    # having maximum prefix sum. 
    msum = arr[0] 
    for i in range(1, maxx, 1): 
        arr[i] += arr[i - 1] 
        if (msum < arr[i]): 
            msum = arr[i] 
            ind = i 
            
    return ind 
      
T = int(input())
for _ in range(T):
  n = int(input())
  left = [int(x) for x in input().split()]
  right = [int(x) for x in input().split()]
  m = max(right)

  print(maxOccured(left,right,n,m)) 
