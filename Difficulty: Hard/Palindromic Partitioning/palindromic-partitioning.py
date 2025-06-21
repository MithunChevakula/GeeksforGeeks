#User function Template for python3

class Solution:
    def palPartition(self, s):
        # code here
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Precompute all palindromic substrings
        for i in range(n):
            is_palindrome[i][i] = True  # single character
        for length in range(2, n + 1):  # substrings of length 2 to n
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = is_palindrome[i + 1][j - 1]

        # dp[i] = min cuts needed for substring s[0..i]
        dp = [0] * n
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n - 1]