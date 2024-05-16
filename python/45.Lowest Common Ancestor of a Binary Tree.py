# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        if root.val == p.val or root.val==q.val: return root
        l_res = self.lowestCommonAncestor(root.left,p,q)
        r_res = self.lowestCommonAncestor(root.right,p,q)
        if l_res and r_res: return root
        return l_res if l_res else r_res

#time =o(n)
#space = o(1)
# i have read explanation 