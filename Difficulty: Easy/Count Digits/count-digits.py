#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        cnt=0
        temp=n
        while(n!=0):
            ld=n%10
            if ld!=0 and temp%ld==0:
                cnt+=1
            n=n//10
        return cnt

 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends