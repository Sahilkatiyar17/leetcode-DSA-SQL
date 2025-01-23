# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        rootL = root.left
        rootR = root.right
        
        lefttree = height(rootL)
        righttree = height(rootR)
        
        left_diameter = self.diameterOfBinaryTree(rootL)
        right_diameter = self.diameterOfBinaryTree(rootR)
        
        # The diameter for the current node is lefttree + righttree
        # The result should be the maximum of current diameter and diameters from subtrees
        return max(lefttree + righttree, left_diameter, right_diameter)
