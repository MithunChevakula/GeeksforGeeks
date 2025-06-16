import heapq

class Solution:
    
   def minCost(self, arr):
    # code here
    heapq.heapify(arr)
    cost, _sum = 0, 0
    while len(arr) > 1:
        _item_1 = heapq.heappop(arr)
        _item_2 = heapq.heappop(arr)
        _sum = _item_1 + _item_2
        cost += _sum
        heapq.heappush(arr, _sum)
    return cost