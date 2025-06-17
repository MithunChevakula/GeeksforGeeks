class Solution:
    def lis(self, arr):
        # code here
        n = len(arr)
        LIS = [1] * n
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
       
