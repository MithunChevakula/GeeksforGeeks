# Link list Node
# class Node:

#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        # code here
        dummy = w = Node(0)
        m = {}
        
        while head:
            if head not in m:
                m[head] = Node(head.data)
            cur = m[head]
            if head.random and head.random not in m:
                m[head.random] = Node(head.random.data)
            cur.random = m.get(head.random, None)
            w.next = cur
            
            w = w.next
            head = head.next
        return dummy.next