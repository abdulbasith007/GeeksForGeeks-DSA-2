def reverse(arr,n,k):
    
    return arr[k:] + arr[:k]
    
tot = int(input())
for _ in range(tot):
    n,k = list(int(x) for x in input().split())
    arr = [int(i) for i in input().split()]
    res = reverse(arr,n,k)
    for x in res:
        print(x, end = ' ')
    print()
    
