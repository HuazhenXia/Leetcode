class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.cur = root 

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return self.cur or self.stack 

    """
    @return: return next node
    """
    def next(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        
        self.cur = self.stack.pop()
        nxt = self.cur
        self.cur = self.cur.right
        return nxt.val