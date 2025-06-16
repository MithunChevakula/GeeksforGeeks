
class Solution:
    def isBalanced(self, s):
        # code here
        ls = []  
        d = {'{':'}','[':']','(':')'}
        
        for char in s:
            if char in d:
                ls.append(char)
            else:
                if not ls or d[ls.pop()] != char:
                    return False
        if ls:
            return False
        return True