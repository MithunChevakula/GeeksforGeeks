#function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def reverseList(self, head):
        # Code here
        p=None
        c=head
        n=head.next
        while n:
            c.next=p
            p=c
            c=n
            n=n.next
        c.next=p
        return c