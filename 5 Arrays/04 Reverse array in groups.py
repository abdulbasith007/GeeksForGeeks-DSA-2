
def reverse(arr, low, high):
  # low = 0
  # high = len(arr) - 1

  while low<high:
    arr[low], arr[high] = arr[high], arr[low]
    low += 1
    high -= 1

  return arr
 
def reverseInGroups(arr,n,k):
    low = 0
    high = k-1
    
    for i in range(0,n,k):
        reverse(arr,low,high)
        low += k
        x = high + k
        if x < n:
          high += k
        else:
          high = n-1

    return arr

arr = [1,2,3,4,5,6,7,8,9,10]
print(reverseInGroups(arr,10,3))


########################################################
__CPP VERSION:__
########################################################


vector<long long> reverseInGroups(vector<long long> mv, int n, int k){
    for (int i = 0; i < n; i += k)
{
int left = i;

// to handle case when k is not multiple of n
int right = min(i + k - 1, n - 1);
int temp=0;
// reverse the sub-array [left, right]
while (left < right){
temp=mv[left];
mv[left] = mv[right];
mv[right]=temp;
left+=1;
right-=1;
}
}

return mv;    
}
