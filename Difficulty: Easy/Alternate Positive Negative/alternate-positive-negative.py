#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        p = []
        q = []
        for x in arr:
            if x>=0:
                p.append(x)
            else:
                q.append(x)
        i = 0
        j = 0
        k = 0
        while i<len(p) and j<len(q):
            if k%2==0:
                arr[k] = p[i]
                i +=1
            else:
                arr[k] = q[j]
                j +=1
            k+=1
        while i<len(p):
            arr[k]=p[i]
            k +=1
            i+=1
        while j<len(q):
            arr[k]=q[j]
            k +=1
            j+=1
        
        return arr