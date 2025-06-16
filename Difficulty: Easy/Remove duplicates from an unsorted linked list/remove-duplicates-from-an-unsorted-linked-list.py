'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        _head = head
        prev = None
        _set = set()
        while _head:
            if _head.data not in _set:
                _set.add(_head.data)
                prev = _head
            else:
                prev.next = prev.next.next
            _head = _head.next
        return head 