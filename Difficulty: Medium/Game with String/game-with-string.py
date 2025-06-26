from heapq import *
from collections import Counter
class Solution:
    def minValue(self, s, k):
        ctr=Counter(s)
        heap=[-i for i in ctr.values()]
        heapify(heap)
        while(heap and k):
            num=heappop(heap)
            num+=1
            k-=1
            if num<0: heappush(heap,num)
        res=0
        for i in heap:
            res+=i**2
        return res