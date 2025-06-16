class Solution:
    def sortedInsert(self, head, key):
        # code here
        # return head of edited linked list
        if head.data>key:
            NewNode=Node(key)
            NewNode.next=head
            return NewNode
        _head=head    
        while head:
            if head.data<key:
                previous=head
                head=head.next
                
            else:
                NewNode=Node(key)
                NewNode.next=previous.next
                previous.next=NewNode
                return _head
        NewNode=Node(key)
        previous.next=NewNode
        return _head