#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        n=len(start)
        lis = []
        for i in range(0, n):
            lis.append((start[i], end[i]))
        lis.sort(key = lambda x : x[1])
        ans = -1
        count = 0
        for st, en in lis:
            if st > ans:
                ans = en
                count += 1
        return count