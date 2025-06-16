'''
	A linked list node has the following structure
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        first = head

        second = head

        

        # Move the first pointer k steps ahead

        for _ in range(k):

            if first is None:

                return -1 # k is greater than the length of the list

            first = first.next

        

        # Move both pointers until first reaches the end

        while first:

            first = first.next

            second = second.next

        

        return second.data if second else -1