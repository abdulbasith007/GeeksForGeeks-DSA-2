# Division rule:

# Here, We will use the formula Dividend = Divisor * Quotient + Remainder
# where Divisor = size of array
#           Quotient = New number at index i after rearrangement
#           Remainder = Old Number at index i before rearrangement
#           Dividend = The number stored at index i
# While Traversing the array, we will Look for the value at arr[arr[i]] (which is to be stored at index i), multiply it with Divisor (size of array), and add the old value present at arr[i] to it.
# Dvisor is a value which is higher then values in array (in this case n - size of array, as array elements are between 0 to n-1)

# Obviously, don't forget to remove the multiplier n from the values while accessing and outputting the new values.


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
