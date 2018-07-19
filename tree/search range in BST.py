class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order 
    """
    def searchRange(self, root, k1, k2):
        result = []
        if root is None:
            return result
        queue = [root]
        
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node.val >= k1 and node.val <= k2:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return sorted(result)