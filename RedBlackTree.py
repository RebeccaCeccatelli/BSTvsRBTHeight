from RBTNode import RBTNode
from BinarySearchTree import BinarySearchTree

import numpy as np

class RedBlackTree(BinarySearchTree):       #inherits from BinarySearchTree

    def setRoot(self, newNode):
        self.root = newNode
        self.root.color = "black"

    #equivalent of insert() in BinarySearchTree
    def rbInsert(self, newNode):        #calls helper method rbInsertFixup()
        self.Tnil = RBTNode(np.inf)      #creates sentinel node Tnil
        self.Tnil.color = "black"
        newNode.left = self.Tnil
        newNode.right = self.Tnil

        self.insert(newNode)
        newNode.color = "red"
        self.rbInsertFixup(newNode)

    def rbInsertFixup(self, insertedNode):      #calls helper methods leftRotate() and rightRotate()
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

    def inOrderWalk(self):      #calls helper method _inOrder()
        self._inOrder(self.root)

    def _inOrder(self,v):
        if v is None:
            return
        if v.left is not None:
            self._inOrder(v.left)
        if v.key != np.inf:
            print(v.key, v.color)
        if v.right is not None:
            self._inOrder(v.right)

    def insert(self,newNode):       #calls helper methods setRoot() and insertNode()
        if self.root is None:
            self.setRoot(newNode)
        else:
            self.insertNode(self.root, newNode)

    def insertNode(self, currentNode, newNode):     #recursive method
        if newNode.key <= currentNode.key:
            if currentNode.left.key != np.inf:       #moves down the tree until sentinel nodes
                self.insertNode(currentNode.left, newNode)
            else:
                currentNode.left = newNode
                newNode.father = currentNode
        elif newNode.key > currentNode.key:
            if currentNode.right.key != np.inf:
                self.insertNode(currentNode.right, newNode)
            else:
                currentNode.right = newNode
                newNode.father = currentNode

    def computeHeight(self, v):     #recursive method
        if self.root is not None:
            if v.key == np.inf:      #finds sentinel node
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
