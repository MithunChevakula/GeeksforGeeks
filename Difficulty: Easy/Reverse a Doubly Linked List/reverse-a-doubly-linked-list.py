'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        while head:
            head.next, head.prev = head.prev, head.next
            if not head.prev:return head
            head=head.prev