import unittest
from BinarySearchTree import BinarySearchTree
from BSTNode import BSTNode
from RBTNode import RBTNode
from RedBlackTree import RedBlackTree
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt


class Experiments(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
    def test_else(self):
        self.assertEqual(13,13)

    def testWorstCase(self):
        firstX,firstY = self.arrays()
        secondX, secondY = self.arrays()
        thirdX, thirdY = self.arrays()
        fourthX, fourthY = self.arrays()
        medianX = []
        medianY = []
        i=0
        while i<100:
            medianX = (firstX[i] + secondX[i] + thirdX[i] + fourthX[i])/4
            medianY = (firstY[i] + secondY[i] + thirdY[i] + fourthY[i])/4
            i +=1
        plt.plot(medianX,medianY) #non si vede nulla FIXME
        plt.show()

    def arrays(self):
        X = np.arange(0,100,1)  # fare molte volte questo stesso test e poi fare il plot sulla media
        Y = []
        for x in X:
            Y.append(self._bsthelper(x))
        return X,Y

    def _bsthelper(self,n):
        bst = BinarySearchTree()
        for x in range (1,n-1,1):
            bst.insert(BSTNode(x))
        start = timer()
        bst.insert(BSTNode(n))
        end = timer()
        return end-start

if __name__ == '__main__':
    unittest.main()
