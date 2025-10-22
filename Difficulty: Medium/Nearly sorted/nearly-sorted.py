class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        from heapq import heappush, heappop
        q = []
        i = 0
        for e in arr:
            heappush(q, e)
            if len(q) > k:
                arr[i] = heappop(q)
                i += 1
        while q:
            arr[i] = heappop(q)
            i += 1