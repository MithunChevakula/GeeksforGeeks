class Solution:
    def delete_node(self, head, x):
        #code here
        cnt = 1
        current = head
        # prev = head
        while cnt < x:
            current = current.next
            cnt +=1
        
        prev = current.prev
        if prev == None:
            ne = current.next
            ne.prev = None
            head = ne
        else:
            prev.next = current.next
            ne = current.next
            if ne != None:
                ne.prev = prev
        
        return head