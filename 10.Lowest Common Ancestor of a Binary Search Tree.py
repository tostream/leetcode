# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findlca(node):
            if node is None: return None
            if node.val >= p.val and node.val < q.val:
                return node
            if node.val < p.val:
                return findlca(node.right)
            if node.val > q.val:
                return findlca(node.left)
        return findlca(root)
#giveup