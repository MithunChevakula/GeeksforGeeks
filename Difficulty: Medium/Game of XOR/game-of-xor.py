class Solution:
    def subarrayXor(self, arr):
        # code here 
        from operator import xor
        from functools import reduce
        if len(arr) & 1:
            return reduce(xor, arr[::2])
        else:
            return 0