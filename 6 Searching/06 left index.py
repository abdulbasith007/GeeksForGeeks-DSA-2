# O(N) Solution:

def leftIndex(n,arr,x):
    for i in range(n):
        if arr[i] == x:
            return i
            
    return -1

#______________________________________________________________________________________

# O(logN) Solution: Using Binary Search to find the first occurence of the element

def leftIndex(N,A,x):
    lo=0
    hi=N-1
    mid=lo + ((hi-lo)//2)
    
    # binary search find the leftmost index of element
    while lo<=hi:
        mid=lo + ((hi-lo)//2)
        
        # if mid element is the required element, return
        if A[mid]==x and mid==0 or A[mid] == x and A[mid-1]<x:
            return mid
        
        # if mid is less than x, then go for right half
        if x > A[mid]:
            lo=mid+1
        
        # else go for left half
        else:
            hi=mid-1
    
    return -1
