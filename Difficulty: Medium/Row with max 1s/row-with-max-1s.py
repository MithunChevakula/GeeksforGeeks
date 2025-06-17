class Solution:
    def rowWithMax1s(self, arr):
        # code here
        res = []
        for i in range(len(arr)):
            element = arr[i].count(1)
            res.append(element)
        
        # Check if all elements are 0
        if all(count == 0 for count in res):
            return -1
        else:
            return res.index(max(res))