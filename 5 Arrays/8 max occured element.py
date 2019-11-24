# Maximum occured element

def maxOccuringElement(left, right, n):
  arr = [0 for i in range(10)]
  for i in range(n):
    x = left[i]
    arr[x] += 1
  
  print(arr)

  for j in range(n):
    y = right[j]
    arr[y] -= 1

  print(arr)

  add = 0
  for i in range(10):
    add += arr[i]
    arr[i] = add
  print(arr)

  return max(arr)
  

left = [1,2,3]
right = [3,5,7]
print(maxOccuringElement(left,right,3))
