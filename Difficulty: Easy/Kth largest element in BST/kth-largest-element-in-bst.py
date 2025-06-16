# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        #your code here
        def inOrder(root, x):
            elements = []
            if root.left:
                left_elements = inOrder(root.left, x)
                elements += left_elements
            elements.append(root.data)
            if root.right:
                right_elements = inOrder(root.right, x)
                elements += right_elements
            return elements
        return inOrder(root, k)[-k]