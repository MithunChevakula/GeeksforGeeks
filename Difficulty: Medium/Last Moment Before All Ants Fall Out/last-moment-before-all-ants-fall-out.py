class Solution:
    def getLastMoment(self, n, l, r):
        a = max(l) if l else 0
        b = max(n-i for i in r) if r else 0
        return max(a,b)