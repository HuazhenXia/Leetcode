class Solution:
    """
    @param: root: A Tree 
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root): 
        # write your code here
        result = []
        
        if root is None:
            return result
        
        #divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        
        #conquer
        result.append(root.val)
        result += left
        result += right
        return result
        