class Solution:
	def perfectSum(self, arr, k):
        n = len(arr)
        prev = [0] * (k + 1)
        
        # prev[0] = 1
        if arr[0] == 0: prev[0] = 2
        else: prev[0] = 1
        if arr[0] <= k and arr[0] != 0:
            prev[arr[0]] = 1
        
        for i in range(1, n):
            curr = [0] * (k + 1)
            curr[0] = 1
            for target in range(k + 1):
                not_take = prev[target]
                take = 0
                if arr[i] <= target:
                    take = prev[target - arr[i]]
                curr[target] = (take + not_take)
            prev = curr
        
        # print(prev[k])
        return prev[k]