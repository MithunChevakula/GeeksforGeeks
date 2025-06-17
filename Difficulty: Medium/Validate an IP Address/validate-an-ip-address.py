class Solution:
    def isValid(self, s):
        #code here
        l = s.split('.')
        
        if(len(l) == 4):
            for i in l:
                if(i.isdigit()):
                    x = int(i)
                    if(x != 0 and i[0] == '0'):
                        return False
                    elif(x >= 0 and x <= 255):
                        continue
                    else:
                        return False
                else:
                    return False
        else:
            return False
            
        return True