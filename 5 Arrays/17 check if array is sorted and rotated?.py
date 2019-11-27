import sys
def checkRotatedAndSorted(arr, n): 
    minEle = sys.maxsize 
    maxEle = -sys.maxsize - 1
    minIndex = -1
    for i in range(n): 
        if arr[i]< minEle: 
            minEle = arr[i] 
            minIndex = i 
    flag1 = 1
  
    # Check if all elements before  
    # minIndex are in increasing order 
    for i in range(1, minIndex): 
        if arr[i] < arr[i - 1]: 
            flag1 = 0
            break
    flag2 = 2
  
    # Check if all elements after  
    # minIndex are in increasing order 
    for i in range(minIndex + 1, n) : 
        if arr[i] < arr[i - 1]: 
            flag2 = 0
            break
   
    if (flag1 and flag2 and 
        arr[n - 1] < arr[minIndex - 1]):
        return True
    else: 
        return False
