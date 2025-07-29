from collections import defaultdict
class Solution:
    def asciirange(self, s):
        dic=defaultdict(lambda:[-1,-1])
        dp=[]
        sm=0
        for i,ch in enumerate(s):
            dp.append(sm)
            sm+=ord(ch)
            if dic[ch][0]==-1:
                dic[ch][0]=i
            else:
                dic[ch][1]=i
        #print(dp,dic)
        res=[]
        for a,b in dic.values():
            if b!=-1 and a!=b-1:
                res.append(dp[b]-dp[a+1])
        return res    