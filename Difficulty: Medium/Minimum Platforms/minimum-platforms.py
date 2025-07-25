class Solution:
    def minimumPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        
        n = len(arr)
        platforms_needed = 0
        result = 0
        i = 0
        j = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1
            else:
                platforms_needed -= 1
                j += 1
            
            result = max(result, platforms_needed)
        
        return result 