#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isCircular(self, head):
        # Code here
        h1=head
        h1=h1.next
        while h1:
            if h1==head:
                return True
            h1=h1.next
        return False