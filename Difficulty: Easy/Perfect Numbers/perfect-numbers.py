#User function Template for python3

class Solution:
    def isPerfectNumber(self, n):
        # code here
        total = 0
        
        for i in range(1,int(n**0.5)+1):
            if n%i == 0:
                total += i
                
                if i != n//i:
                    total += n//i
                
        return (total-n == n)