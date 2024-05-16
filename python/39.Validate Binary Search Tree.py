# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,lower_bound=-math.inf,upper_boud=math.inf):
            if not node: return True
            if lower_bound < node.val < upper_boud:
                left = dfs(node.left,lower_bound,node.val)
                right = dfs(node.right,node.val,upper_boud)
                return left and right
            else: 
                return False
        return dfs(root)
