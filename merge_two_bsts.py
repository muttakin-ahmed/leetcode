class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        # Assuming the merger is adding the values of the corresponding nodes of root1 and root2  
        root1.val += root2.val
        # If we wanted to get the bigger value
        # root1.val = max(root1.val, root2.val)
        # or the min value would be the same, we would have to use the min function
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
