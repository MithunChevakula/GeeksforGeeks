class Solution:
	def minDifference(self, arr):
        n, total = len(arr), sum(arr)
        dp = [False for _ in range(total + 1)]
        dp[0] = True
        
        # logic for finding subset sum for all values till total as total is the maximum sum
        for i in range(1, n + 1):
            for j in range(total, arr[i-1] - 1, -1):
                dp[j] = dp[j] or dp[j - arr[i-1]]
       
        # dp array now holds true for all the possible subset sums
        result = float('inf')
        for i in range(total + 1):
            if dp[i] == True:
                # we need to minimize s1 - s2 OR total - 2.s2
                result = min(result, abs(total - (2 * i)))
        
        return result