def minAdjDiff(arr, n):
    min = 99999
    for i in range(n-1):
        x = abs(arr[i]-arr[i+1])
        if x < min:
            min = x
       
    z = abs(arr[n-1]- arr[0])     
    if z < min:
        min = z
        
    return min
     
