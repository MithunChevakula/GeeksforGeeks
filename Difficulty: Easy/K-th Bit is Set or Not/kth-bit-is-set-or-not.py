class Solution:
    
    ''' n : int
        k : int
        Return Type : Boolean '''
    def checkKthBit(self, n, k):
        # Your code here
        s = bin(n).replace('0b', '')
        if len(s) <= k:
            return False
        
        return s[-k-1] == '1'
        