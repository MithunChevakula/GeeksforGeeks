import math 
class Solution:
    def smallestDivisor(self, arr, k):
        n = len(arr)
        l , h = 1 , max(arr) 
        
        def isPossible(div):
            return sum([math.ceil(ele/div) for ele in arr]) <= k 
        
        while l <= h : 
            mid = (l + h) // 2 
            if isPossible(mid):
                h = mid -1 
            else: 
                l = mid + 1 
        
        return l 