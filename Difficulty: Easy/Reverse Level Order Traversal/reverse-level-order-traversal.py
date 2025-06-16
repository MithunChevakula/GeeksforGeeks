'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def reverseLevelOrder(self,root):
        # code here
        level = [root]
        _levelOrder = []
        _levels = []
        while level:
            _tmp = []
            while level:
                item = level.pop(0)
                _levels.append(item.data)
                if item.left:
                    _tmp.append(item.left)
                if item.right:
                    _tmp.append(item.right)
            
            _levelOrder = _levels + _levelOrder
            _levels = []
            level = _tmp[:]
        return _levelOrder