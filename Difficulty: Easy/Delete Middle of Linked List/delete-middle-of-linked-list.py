'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:

    def deleteMid(self, head):
        curr=head
        c=0
        while curr:
           c=c+1
           curr=curr.next
        mid=c//2
        co=0
        curr=head
        if c==1:
            return None
        else:
            while curr:
                co+=1
                if co==mid:
                    curr.next=curr.next.next
                curr=curr.next
            return head

