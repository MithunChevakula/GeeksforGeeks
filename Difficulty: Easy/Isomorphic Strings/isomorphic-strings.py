class Solution:
    def areIsomorphic(self,s1,s2):
        # code here
        a={}
        b={}
        for i in s1:
            a[i]=a.get(i,0)+1
        for i in s2:
            b[i]=b.get(i,0)+1
        l1=[]
        l2=[]
        for i in a.values():
            l1.append(i)
        for i in b.values():
            l2.append(i)
        if (l1==l2):
            return True
        return False