class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ori_color = image[sr][sc]
        def dfs(sr,sc,color,ori_color):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]):
                return image
            if image[sr][sc] == color:
                return image
            if image[sr][sc] == ori_color:
                image[sr][sc] = color
                dfs(sr-1,sc,color,ori_color)
                dfs(sr+1,sc,color,ori_color)
                dfs(sr,sc-1,color,ori_color)
                dfs(sr,sc+1,color,ori_color)
        dfs(sr,sc,color,ori_color)
        return image
# i can't explain time complexity, O(n)?