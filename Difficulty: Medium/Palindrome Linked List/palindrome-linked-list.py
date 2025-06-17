'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        res = []
        while head:
            res.append(head.data)
            head = head.next
        for i in range(len(res)//2):
            if res[i] != res[-(i+1)]:
                return False
        return True