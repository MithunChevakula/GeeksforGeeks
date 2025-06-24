class Solution:
    def maxSubseq(self, s, k):
        #code here
        stack = []
        n, cnt = len(s), 0
        # add char to stack
        for c in s:
            # remove char if not in lexicographical sequence
            while stack and cnt < k and stack[-1] < c:
                stack.pop()
                cnt +=1
            stack.append(c)
        # Ensure we only keep the last (n - k) characters
        while len(stack) > n - k:
            stack.pop()
            
        return ''.join(stack)

