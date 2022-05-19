
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.father = None

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children

    def setLeftChild(self, leftChild):
        self.left = leftChild

    def setRightChild(self, rightChild):
        self.right = rightChild

    def getFather(self):
        return self.father

    def setFather(self, father):
        self.father = father

