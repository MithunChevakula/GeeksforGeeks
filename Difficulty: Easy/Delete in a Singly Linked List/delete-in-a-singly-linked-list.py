# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    _loc = 1
    _head = head
    if x == 1:
        _head = head.next
    while head:
        if _loc + 1 == x:
            head.next = head.next.next
        head = head.next
        _loc += 1
    return _head