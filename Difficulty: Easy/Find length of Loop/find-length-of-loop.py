'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #code here
        visited = {}
        temp = head
        index = 0
        
        while temp:
            if temp in visited:
                return index - visited[temp]
            visited[temp] = index
            temp = temp.next
            index += 1
        
        return 0