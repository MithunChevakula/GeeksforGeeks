
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        n1=0
        n2=1
        if n==0:
            return 0
        if n==1:
            return 1
        for _ in range(2,n+1):
            n3=n1+n2
            n1=n2
            n2=n3
        return n3
        
