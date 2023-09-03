# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = {}
        queue = []
        def dfs(node, hight=0):
            if not node: return hight
            hight+=1
            dfs(node.left,hight)
            dfs(node.right,hight)
            temp = result.get(hight,[])
            temp.append(node.val)
            result[hight]=temp
        dfs(root)
        return [result[i] for i in sorted(result.keys())]