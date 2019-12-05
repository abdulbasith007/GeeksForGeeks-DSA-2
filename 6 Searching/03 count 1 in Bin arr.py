# Here we can use Linear Search to count the no. o f1's but in the below code we're finding the first and last occurance of 1

def first(arr,n,k):
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        if mid == 0 or arr[mid] == k and k > arr[mid-1]:
            return mid
        elif arr[mid] > k:
            low = mid+1
        else:
            high = mid - 1
            
    return -1

def last(arr,n,k):
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        
        if mid == n-1 or arr[mid] == k and k > arr[mid+1]:
            return mid
        elif arr[mid] < k:
            high = mid - 1            
        else:
            low = mid+1
            
    return -1
            
    
def countOnes(arr,n):
    a = first(arr,n,1)
    b = last(arr,n,1)
    
    return b-a+1
