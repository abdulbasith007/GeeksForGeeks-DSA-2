# Here the input array is sorted; so, we can use Binary Search
# Output Format: 1 if present else -1

def searchInSorted(arr,n,k):
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == k:
            return 1
        elif arr[mid] > k:
            high = mid-1
        else:
            low = mid+1
            
    return -1
