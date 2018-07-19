class Solution(object):
    def zigzagLevelOrder(self, root):
        queue, result = [], [] 
        
        #base case
        if root is None:
            return result
        
        queue.append(root)
        count = 0
        while queue: #amount of levels
            level = []
            size = len(queue)
            for i in range(size): #elements in each level
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count%2 == 1:
                level.reverse()
            count += 1
            result.append(level)
        
        return result    