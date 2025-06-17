# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        dict1={0:-1}
        sm,ans=0,0
        for i in range(len(arr)):
            sm+=arr[i]
            if sm-k in dict1:
                ans=max(ans,i-dict1[sm-k])
            if sm not in dict1:
                dict1[sm]=i
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends