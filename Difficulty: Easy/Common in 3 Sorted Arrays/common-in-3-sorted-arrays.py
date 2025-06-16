#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        a1=set(arr1)
        a2=set(arr2)
        a3=set(arr3)
        if len(a1)<len(a2):
            a1,a2=a2,a1
        if len(a1)<len(a3):
            a1,a3=a3,a1
        ans=list(a1.intersection(a2).intersection(a3))
        if not ans:
            return [-1]
        else:
            ans.sort()
            return ans