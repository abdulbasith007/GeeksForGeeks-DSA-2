def findFloor(arr,n,x):
    if arr[0] == x:
        return arr[0]
    if arr[0] > x:
        return -1
    for i in range(1,n):
        if arr[i] > x:
            return arr[i-1]
    return arr[n-1]
