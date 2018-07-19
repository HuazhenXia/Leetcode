import sys

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false 
    """
    def isValidBST(self, root):
        return self.bstHelper(root, -sys.maxsize, sys.maxsize)
    
    def bstHelper(self, root, minValue, maxValue):
        if root is None: return True
        if root.val >= maxValue or root.val <= minValue:
            return False
        
        return self.bstHelper(root.left, minValue, root.val) and self.bstHelper(root.right, root.val, maxValue)
        
