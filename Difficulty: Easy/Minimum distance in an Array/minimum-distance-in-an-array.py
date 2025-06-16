class Solution:
    def minDist(self, arr, x, y):
        p = -1
        q = -1
        min_dist = float('inf')
        for i in range(len(arr)):
            if arr[i] == x:
                p = i
                if q != -1:
                    min_dist = min(min_dist, abs(p-q))
            elif arr[i] == y:
                q = i
                if p != -1:
                    min_dist = min(min_dist, abs(q-p))
        if p == -1 or q == -1:
            return -1
            
        return min_dist if min_dist != float('inf') else -1
        
    