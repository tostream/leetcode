# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        checker = {}
        res=[0]
        def dfs (node):
            if not node : return -1
            l_side = dfs(node.left)
            r_side = dfs(node.right)
            hight = max(l_side,r_side)+1
            dia = l_side+ r_side+2
            res[0] = max(res[0],dia)
            return hight
        hight = dfs(root)
        return res[0]