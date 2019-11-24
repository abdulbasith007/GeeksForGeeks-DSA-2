def equilibriumPoint(arr, n):
    
    sum = 0
    for i in range(n):
        sum += arr[i]
    
    leftSum = 0
    for i in range(n):
        sum -= arr[i]
        if sum == leftSum:
            return i+1
        leftSum += arr[i]    
        
    return -1
