class Solution:
    def findExtra(self,a,b):
        #add code here
        minimum_length=min(len(a), len(b))
        for i in range(0, minimum_length):
            if a[i]!=b[i]:
                return i
        return minimum_length