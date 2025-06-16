''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self,head1,head2):
        #return head
        ref=head2
        dummy=Node(0)
        temp=dummy
        itr=head1
        while itr and ref:
            if itr.data==ref.data:
                temp.next=Node(itr.data)
                temp=temp.next
                ref=ref.next
                itr=itr.next
            elif itr.data>ref.data:
                ref=ref.next
            else:
                itr=itr.next
        return dummy.next