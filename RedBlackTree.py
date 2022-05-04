from RBTNode import RBTNode
from BinarySearchTree import BinarySearchTree


class RedBlackTree(BinarySearchTree):

    def setRoot(self, newNode):
        self.root = newNode
        self.root.color = "black"

    def rbInsertFixup(self, insertedNode):
        if insertedNode.father is not None:
            finished = False
            while not finished and insertedNode.father.color == "red":
                if insertedNode.father == insertedNode.father.father.left:
                    uncle = insertedNode.father.father.right
                    if uncle.color == "red":
                        insertedNode.father.color = "black"
                        uncle.color = "black"
                        insertedNode.father.father.color = "red"
                        insertedNode = insertedNode.father.father
                    else:
                        if insertedNode == insertedNode.father.right:
                            insertedNode = insertedNode.father
                            self.leftRotate(insertedNode)
                        insertedNode.father.color = "black"
                        insertedNode.father.father.color = "red"
                        self.rightRotate(insertedNode.father.father)
                elif insertedNode.father == insertedNode.father.father.right:
                    uncle = insertedNode.father.father.left
                    if uncle.color == "red":
                        insertedNode.father.color = "black"
                        uncle.color = "black"
                        insertedNode.father.father.color = "red"
                        insertedNode = insertedNode.father.father
                    else:
                        if insertedNode == insertedNode.father.left:
                            insertedNode = insertedNode.father
                            self.rightRotate(insertedNode)
                        insertedNode.father.color = "black"
                        insertedNode.father.father.color = "red"
                        self.leftRotate(insertedNode.father.father)
                if insertedNode == self.root:
                    finished = True
        self.root.color = "black"

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.father = x
        y.father = x.father
        if x.father is None:
            self.root = y
        elif x is x.father.left:
            x.father.left = y
        else:
            x.father.right = y
        y.left = x
        x.father = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.father = x
        y.father = x.father
        if x.father is None:
            self.root = y
        elif x is x.father.right:
            x.father.right = y
        else:
            x.father.left = y
        y.right = x
        x.father = y

    def rbInsert(self, newNode):
        self.Tnil = RBTNode(10000)
        self.Tnil.color = "black"
        newNode.left = self.Tnil
        newNode.right = self.Tnil
        self.insert(newNode)
        newNode.color = "red"
        self.rbInsertFixup(newNode)

    def inOrderWalk(self):
        self._inOrder(self.root)

    def _inOrder(self,v):
        if v is None:
            return
        if v.left is not None:
            self._inOrder(v.left)
        if v.key is not 10000:
            print(v.key, v.color)
        if v.right is not None:
            self._inOrder(v.right)

    def insert(self,newNode):
        if self.root is None:
            self.setRoot(newNode)
        else:
            self.insertNode(self.root, newNode)

    def insertNode(self, currentNode, newNode):
        if newNode.key <= currentNode.key:
            if currentNode.left.key is not 10000:
                self.insertNode(currentNode.left, newNode)
            else:
                currentNode.left = newNode
                newNode.father = currentNode
        elif newNode.key > currentNode.key:
            if currentNode.right.key is not 10000:
                self.insertNode(currentNode.right, newNode)
            else:
                currentNode.right = newNode
                newNode.father = currentNode

    def computeHeight(self, v):
        if self.root is not None:
            if v.key is 10000:
                return -1
            else:
                leftHeight = -1
                rightHeight = -1
                if v.left is not None:
                    leftHeight = self.computeHeight(v.left)
                if v.right is not None:
                    rightHeight = self.computeHeight(v.right)

                max = leftHeight
                if rightHeight > leftHeight:
                    max = rightHeight
                return max + 1
