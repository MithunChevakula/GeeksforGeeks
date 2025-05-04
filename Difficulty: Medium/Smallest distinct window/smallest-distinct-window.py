#User function Template for python3
from collections import defaultdict
class Solution:
    def findSubString(self, str):
        # code here
        ans = n = len(str) # whole string is maximum sized window containing all letters
        k = len(set(str)) # number of unique letters
        d = defaultdict(int) # dict with 'int' as defaultfactory
        i = 0
        for j,char in enumerate(str):
            if not d[char]: # first entry
                k -= 1
            d[char] += 1
            while not k: # d contains all unique letters of str
                ans = min(ans, j-i+1)
                d[str[i]] -= 1
                if not d[str[i]]:
                    k = 1 # equivalent to k += 1
                i += 1
        return ans


    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends