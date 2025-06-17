#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        combine = a + b
        combine.sort()  
        return combine[k-1] 
