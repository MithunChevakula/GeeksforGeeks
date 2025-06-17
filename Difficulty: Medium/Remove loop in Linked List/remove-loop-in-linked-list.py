'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        _set = set()
        _removed = False
        prev = head
        while head:
            if head not in _set:
                _set.add(head)
                prev = head
                head = head.next
            else:
                prev.next = None
                _removed = True
                break
        return _removed