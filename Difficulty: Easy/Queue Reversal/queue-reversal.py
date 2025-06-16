class Solution:
    #Function to reverse the queue.
    def reverseQueue(self, q):
        # code here
        stack=[]
        while not q.empty():
            stack.append(q.get())
        while stack:
            q.put(stack.pop())
        return q