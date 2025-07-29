class Solution:
    def maxWater(self, arr):
        n = len(arr)
        lmax = [0] * n
        rmax = [0] * n
        trpWater = 0
        
        lmax[0] = arr[0]
        for i in range(1, n-1):
            lmax[i] = max(arr[i], lmax[i-1])
        
        rmax[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            rmax[i] = max(arr[i], rmax[i+1])
            
        for i in range(1, n-1):
            waterLvl = min(lmax[i], rmax[i])
            trpWater += waterLvl - arr[i]
            
        return trpWater