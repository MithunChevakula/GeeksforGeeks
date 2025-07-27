class Solution:
    def isPerfect(self, n):
        # code here
        s = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                s += i
                if i != n // i:
                    s += n//i
        if n == s-n:
            return True
        return False