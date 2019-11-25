def div(arr,n):
  maxi = n-1
  mini = 0
  
  me = arr[n-1] + 1
  for i in range(n):
    if i & 1:
      arr[i] += (arr[mini]%me)*me
      mini += 1

    else:
      arr[i] += (arr[maxi]%me)*me
      maxi -= 1
    
  
  for i in range(n):
    arr[i] //= me
  
  
  return arr
