# This problem can be further optimized and can be done in O(1) space using Moore's Voting Algorithm 

def majorityElement(arr,n):
      dict = {}
      for i in range(n):
        dict[arr[i]] = dict.get(arr[i],0) + 1
    
      maxValue = 0
      
      x = 0
      for i in dict:
          if dict[i] != 1:
              x += 1
      if x == 0:
          return -1
        
      for i in dict:
        if dict.get(i) > maxValue:
          max = i
          maxValue = dict[i]
          if maxValue > n//2:
              return max
              
      return -1
