#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        temp=n
        res=0
        while(n>0):
            rem=n%10
            res+=rem**3
            n//=10
        if res==temp:
            return True
        return False