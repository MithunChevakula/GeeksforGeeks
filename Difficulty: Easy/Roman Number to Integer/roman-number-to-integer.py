#User function Template for python3

class Solution:
    def romanToDecimal(self, s): 
        # code here
        rom={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        i=0
        while i<len(S):
            if i+1<len(S) and rom[S[i]]<rom[S[i+1]]:
                res+=rom[S[i+1]]-rom[S[i]]
                i+=2
            else:
                 res+=rom[S[i]]
                 i+=1
        return res