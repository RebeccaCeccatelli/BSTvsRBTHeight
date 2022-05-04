import unittest

from BSTNode import BSTNode
from BinarySearchTree import BinarySearchTree
from RBTNode import RBTNode
from RedBlackTree import RedBlackTree

import numpy as np
from matplotlib import pyplot as plt
from timeit import default_timer as timer

class MyTestCase(unittest.TestCase):
    def testComputeBSTHeight(self):
        A = [13,15,7,6,2,20,18,1,9,52]
        bstA = BinarySearchTree()
        for x in A:
            bstA.insert(BSTNode(x))
        heightA = bstA.computeHeight(bstA.root)
        self.assertEqual(heightA, 4, "heightA should be 4.")

        B = [27,1,6,-54,22,34,30,132,0]
        bstB = BinarySearchTree()
        for x in B:
            bstB.insert(BSTNode(x))
        heightB = bstB.computeHeight(bstB.root)
        self.assertEqual(heightB, 3, "heightB should be 3.")

        C = [10,9,8,7,6,5,4,3,2,1]
        bstC = BinarySearchTree()
        for x in C:
            bstC.insert(BSTNode(x))
        heightC = bstC.computeHeight(bstC.root)
        self.assertEqual(heightC, 9, "heightC should be 9.")

    def testComputeRBTHeight(self):
        A = [13,15,7,6,2,20,18,1,9,52]
        rbtA = RedBlackTree()
        for x in A:
            rbtA.rbInsert(RBTNode(x))
        heightA = rbtA.computeHeight(rbtA.root)
        self.assertEqual(heightA, 3, "heightA should be 3.")

        B = [27,1,6,-54,22,34,30,132,0]
        rbtB = RedBlackTree()
        for x in B:
            rbtB.rbInsert(RBTNode(x))
        heightB = rbtB.computeHeight(rbtB.root)
        self.assertEqual(heightB, 3, "height should be 3.")

        C = [10,9,8,7,6,5,4,3,2,1]
        rbtC = RedBlackTree()
        for x in C:
            rbtC.rbInsert(RBTNode(x))
        heightC = rbtC.computeHeight(rbtC.root)
        self.assertEqual(heightC, 4, "height should be 4.")

    def testWorstCaseInBST(self):
        N = np.arange(1,960,1)
        BSTHeight = []

        for n in N:
            bst = BinarySearchTree()
            values = np.arange(1,n+1,1)
            for value in values:
                bst.insert(BSTNode(value))
            height = bst.computeHeight(bst.root)
            BSTHeight.append(height)
            self.assertEqual(height, n-1)

        plt.plot(N, BSTHeight)
        plt.xlabel("n")
        plt.ylabel("bstHeight")
        plt.show()

    def testWorstCaseInRBT(self):
        N = np.arange(1,960,1)
        RBTHeight = []

        for n in N:
            rbt = RedBlackTree()
            values = np.arange(1,n+1,1)
            for value in values:
                rbt.rbInsert(RBTNode(value))
            height = rbt.computeHeight(rbt.root)
            RBTHeight.append(height)
            self.assertLess(height, 2*np.log2(n+1))

        plt.plot(N,RBTHeight, 'g', 1.7*np.log2(N), 'r')
        plt.xlabel("n")
        plt.ylabel("rbtHeight")
        plt.show()

    def testPlotBothHeights(self):
        BSTHeight = []
        RBTHeight = []

        N = np.arange(1,200,1)
        for n in N:
            bst = BinarySearchTree()
            rbt = RedBlackTree()

            values = np.arange(1,n+1,1)
            for value in values:
                bst.insert(BSTNode(value))
                rbt.rbInsert(RBTNode(value))

            BSTHeight.append(bst.computeHeight(bst.root))
            RBTHeight.append(rbt.computeHeight(rbt.root))

        plt.plot(N,BSTHeight,'r', N, RBTHeight, 'g')
        plt.show()

    def testTimeComplexity(self):
        maxValue = 400
        N = np.arange(0,maxValue,1)
        bstComplexity = [0]*maxValue
        rbtComplexity = [0]*maxValue

        i = 0
        for times in range (0,200,1):
            bst = BinarySearchTree()
            rbt = RedBlackTree()

            for n in N:
                start1 = timer()
                bst.insert(BSTNode(n))
                end1 = timer()

                start2 = timer()
                rbt.rbInsert(RBTNode(n))
                end2 = timer()

                bstComplexity[n] += end1-start1
                rbtComplexity[n] += end2-start2
                i +=1

        for value in bstComplexity:
            value /= i
        for value in rbtComplexity:
            value /=i

        plt.plot(N,bstComplexity, 'r', N, rbtComplexity,'g')
        plt.show()

if __name__ == '__main__':
    unittest.main()
