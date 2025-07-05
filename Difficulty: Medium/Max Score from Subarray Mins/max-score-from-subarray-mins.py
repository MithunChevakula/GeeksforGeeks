class Solution:
    def maxSum(self, arr):
        # code here
        ans = float('-inf')
        for i in range(len(arr)-1):
            if arr[i]+arr[i+1]>ans:
                ans = arr[i]+arr[i+1]
        return ans
    
