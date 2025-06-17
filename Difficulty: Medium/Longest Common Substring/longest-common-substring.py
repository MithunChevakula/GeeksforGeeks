class Solution:
    def longestCommonSubstr(self, text1, text2):
        n = len(text1)
        m = len(text2)

        prev = [0] * (m + 1)
        cur = [0] * (m + 1)

        ans = 0    

        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    cur[ind2] = 1 + prev[ind2 - 1]
                    ans = max(ans, cur[ind2])
                else:
                    cur[ind2] = 0 
            prev = cur[:]        
        return ans  