#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        # Your code goes here
        pos = [ele for ele in arr if ele >= 0]
        neg = [ele for ele in arr if ele < 0]
        pos.extend(neg)
        arr[:] = pos[:] # as result should be only arr
        return pos