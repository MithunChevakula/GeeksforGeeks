"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        # code here
        if head.next is None:
            return head
        # Add a temp head for prev-value
        new_node = Node(-1)
        new_node.next = head
        head = new_node
        # Keep count of pairs using prev, curr and next-node values 
        prev = head
        curr = prev.next
        next_node = curr.next
        while next_node and curr:
            prev.next = next_node
            curr.next = next_node.next
            next_node.next = curr
            prev = curr
            curr = curr.next
            if curr is None:
                break
            next_node = curr.next
        # Remove temp-head from LL
        head = new_node.next
        return head