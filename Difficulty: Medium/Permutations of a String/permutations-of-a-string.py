#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        def solve(s, ind, ans):
            if ind == len(s):
                ans.append(''.join(s))
                return
            seen = set()
            for i in range(ind, len(s)):
                if s[i] in seen:
                    continue  # skip duplicate characters at this position
                seen.add(s[i])
                s[ind], s[i] = s[i], s[ind]
                solve(s, ind + 1, ans)
                s[ind], s[i] = s[i], s[ind]  # backtrack

        chars = list(s)
        ans = []
        solve(chars, 0, ans)
        return ans


        
