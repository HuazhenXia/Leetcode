class Solution:
    """
    @param: root: The root of binary tree.
    @return: An integer 
    """
    def maxPathSum(self, root):
        # write your code here
        maxSum, _ = self.maxPathHelper(root)
        return maxSum
        
    def maxPathHelper(self, root):
        if root is None:
            return None, 0
        
        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        single = max(left[1] + root.val, right[1] + root.val, 0)
        maxpath = max(left[0], right[0], root.val + left[1] + right[1])
        
        return maxpath, single
        