# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        _head = head
        _tail = _head
        count = 1
        while _tail.next:
            _tail = _tail.next
            count += 1
        k = k % count
        for _ in range(k):
            tmp = _head
            if _head.next:
                _head = _head.next
                tmp.next = None
                _tail.next = tmp
                _tail = _tail.next

        return _head