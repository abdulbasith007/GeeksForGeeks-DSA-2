# As the input is not Ascending or Descending, we're using Linear Search. For sorted arrays, Binary Search will do the work in logn time.  

def linearSearch(arr,n,k):
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            high = mid-1
        else:
            low = mid+1

for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())
    print(linearSearch(arr,n,k))
