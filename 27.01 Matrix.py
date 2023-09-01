class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        result = [ [-1] * m for _ in range(n)]
        queue = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i,j))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            x,y = queue.pop(0)
            for dx , dy in directions:
                check_x = x+dx
                check_y = y+dy
                if 0 <= check_x < n and 0 <= check_y < m and result[check_x][check_y] < 0:
                    result[check_x][check_y] = result[x][y] + 1
                    queue.append((check_x,check_y))
        return result