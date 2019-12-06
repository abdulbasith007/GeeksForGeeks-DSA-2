def leftIndex(n,arr,x):
    for i in range(n):
        if arr[i] == x:
            return i
            
    return -1
