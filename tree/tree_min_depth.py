"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None 
"""
class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if root.left is None or root.right is None:
            return max(left, right)+1

        return min(left, right)+1
        