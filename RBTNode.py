from BSTNode import BSTNode

class RBTNode(BSTNode):     #inherits from BSTNode
    def __init__(self, key):
        super().__init__(key)
        self.color = None

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


