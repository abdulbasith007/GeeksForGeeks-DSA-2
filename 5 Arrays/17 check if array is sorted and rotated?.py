def checkRotatedAndSorted(arr,n):
    mini = 9999
    for i in range(n):
        if arr[i] < mini:
            mini = arr[i]
            
    for i in range(mini, n-1):
        if arr[i] < arr[i+1]:
            flag = True
        else:
            flag = False
            break
        
    for i in range(0, mini-1):
        if arr[i] < arr[i+1]:
            flag = True
        else:
            flag = False
            break
        
    maxj = -9999
    for j in range(n):
        if arr[j] > maxj:
            maxj = arr[j]
            
    for j in range(maxj, n-1):
        if arr[j] > arr[j+1]:
            flag1 = True
        else:
            flag1 = False
            break
        
    for j in range(0, maxj-1):
        if arr[j] > arr[j+1]:
            flag1 = True
        else:
            flag1 = False
            break
    
    if flag or flag1:
        return True
    return False
        
            
            
