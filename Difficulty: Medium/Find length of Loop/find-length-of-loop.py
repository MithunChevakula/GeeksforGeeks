'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, lund):
        #code here
        chut = {}
        size = 1
        while lund:
            if lund in chut:
                return size - chut.get(lund)
            
            chut[lund] = size
            size += 1
            lund = lund.next
        
        return 0