#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        p=0
        while n:
            p=p+1
            if n&1==1:
                return p
            n=n>>1    
        return 0