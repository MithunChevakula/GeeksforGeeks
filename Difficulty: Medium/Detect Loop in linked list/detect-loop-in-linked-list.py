'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
# Return boolean value True or False

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        _set = set()
        detact = False
        while head:
            if head not in _set:
                _set.add(head)
                head = head.next
            else:
                detact = True
                break
        return detact