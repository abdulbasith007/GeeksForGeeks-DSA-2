#You are given an array arr[] of size N. You are also given two elements x and y. Now, you need to tell which element (x or y) appears most in the array. In other words, return the element, x or y, that has higher frequency in the array. If both elements have the same frequency, then just return the smaller element.

# NOTE :  We need to return the elements, not their counts.

def majorityWins(arr, n,  x,y):
    cnt1,cnt2 = 0,0
    for i in range(n):
        if arr[i] == x:
            cnt1+=1
        if arr[i] == y:
            cnt2+=1
        
    if cnt1 > cnt2:
        return x
    elif cnt2 > cnt1:
        return y
    else:
        return min(x,y)
