# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxdepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Check the depth of the left and right subtrees
        lefttree = self.maxdepth(root.left)
        righttree = self.maxdepth(root.right)
        
        # Check the balance condition for the current node
        if abs(lefttree - righttree) > 1:
            return False
        
        # Recursively check for left and right subtrees
        return self.isBalanced(root.left) and self.isBalanced(root.right)

        
        
        