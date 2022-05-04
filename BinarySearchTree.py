from BSTNode import BSTNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,newNode):
        if self.root is None:
            self.setRoot(newNode)
        else:
            self.insertNode(self.root, newNode)

    def setRoot(self, newNode):
        self.root = newNode

    def insertNode(self, currentNode, newNode):
        if newNode.key <= currentNode.key:
            if currentNode.left:
                self.insertNode(currentNode.left, newNode)
            else:
                currentNode.left = newNode
                newNode.father = currentNode
        elif newNode.key > currentNode.key:
            if currentNode.right:
                self.insertNode(currentNode.right, newNode)
            else:
                currentNode.right = newNode
                newNode.father = currentNode

    def recursiveSearch(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if currentNode is None:
            return False, None
        elif key == currentNode.key:
            return True, currentNode
        elif key < currentNode.key:
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    def inOrderWalk(self):
        self._inOrder(self.root)

    def _inOrder(self,v):
        if v is None:
            return
        if v.left is not None:
            self._inOrder(v.left)
        print(v.key)
        if v.right is not None:
            self._inOrder(v.right)

    def getMaximum(self, currentNode):
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode

    def computeHeight(self, v):
        if v is None:
            return -1
        else:
            leftHeight = self.computeHeight(v.left)
            rightHeight = self.computeHeight(v.right)
            return max(leftHeight, rightHeight) + 1
