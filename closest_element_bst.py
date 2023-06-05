# Given a BST and an integer. Find the least absolute difference between any node 
# value of the BST and the given integer.

class Solution:
    
    #Function to find the least absolute difference between any node
    #value of the BST and the given integer.
    def minDiff(self,root, K):
        # code here
        # if root is null return a big value
        if root==None:
            return 100000000 
        # it is BST so this can be done in O(h) time ,no need to traverse each node 
        if K>root.data:
            return min(abs(K-root.data),self.minDiff(root.right,K))
        else:
            return min(abs(K-root.data),self.minDiff(root.left,K))
