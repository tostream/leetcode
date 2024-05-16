# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) : 
            if node is None:
                return node
            res = TreeNode(0,node.left,node.right)
            node.right = dfs(res.left)
            node.left = dfs(res.right)
            return node
        return dfs(root)
