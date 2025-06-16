#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        arr.sort()
        i = 0
        j = len(arr)-1
        s = set()
        ls = []
        while i < j:
            if arr[i] + arr[j] == 0:
                if (arr[i],arr[j]) not in s:
                    s.add((arr[i],arr[j]))
                    ls.append([arr[i],arr[j]])
                i +=1
                j -=1
            elif arr[i] + arr[j] < 0:
                i += 1
            else:
                j -= 1
        return sorted(ls)