class Solution:
    def reverseFirstK(self, q, k):
        #code here
        n = len(q)
        if k    > n or k <= 0:
            return q
        temp = []
        for i in range(k):
            temp.append(q[i])
        re = []
        for i in range(k):
            re.append(temp.pop())
        for i in range(k, n):
            re.append(q[i])
        return re