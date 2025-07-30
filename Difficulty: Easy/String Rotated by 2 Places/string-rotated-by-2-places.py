class Solution:
    def isRotated(self,s1,s2):
        #code here
        s3=s1[2:]+s1[:2]
        s4=s1[-2:]+s1[:-2]
        if s3==s2 or s4==s2:
            return True
        return False
        