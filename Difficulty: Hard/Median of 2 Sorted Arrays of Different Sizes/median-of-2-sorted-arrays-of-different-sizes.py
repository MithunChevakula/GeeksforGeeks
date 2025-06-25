#User function Template for python3

class Solution:
    def medianOf2(self, a, b):
        #code here
        merged = sorted(a+b)
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        else:
            mid1 = merged[ n // 2 - 1]
            mid2 = merged[ n // 2]
        return (mid1 + mid2) / 2