#User function Template for python3

class Solution:
    def maxValue(self, arr): 
        # Complete the function
        arr.sort()
        MOD = 10**9 + 7
        return sum((val * i) % MOD for i, val in enumerate(arr)) % MOD
      
