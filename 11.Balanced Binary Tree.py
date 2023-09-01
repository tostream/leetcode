# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root : return True
        def dfs(node):
            if not node: return -1
            return 1 + max(dfs(node.left),dfs(node.right))
        L_result = dfs(root.left)
        R_result = dfs(root.right)
        res = abs(L_result - R_result)

        return res <  2 and self.isBalanced(root.left) and self.isBalanced(root.right)