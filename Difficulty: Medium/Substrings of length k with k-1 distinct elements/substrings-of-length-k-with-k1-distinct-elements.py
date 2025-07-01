from collections import Counter
class Solution:
    def substrCount(self, s, w):
        res=left=0
        k=w-1
        ctr=Counter()
        cnt=0
        for right,val in enumerate(s):
            ctr[val]+=1
            if ctr[val]==1:
                cnt+=1
            while(cnt>k or right-left+1>w):
                ctr[s[left]]-=1
                if ctr[s[left]]==0:
                    cnt-=1
                left+=1
            if right-left+1==w and cnt==k:
                res+=1
        return res     
        