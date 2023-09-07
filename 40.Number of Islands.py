class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited =set()
        n = len(grid)
        m= len(grid[0])
        res = 0
        def bfs(x, y):
            queue = [(x,y)]
            directions =[[0,1],[1,0],[0,-1],[-1,0]]
            visited.add((x,y))
            while queue:
                row,col = queue.pop(0)
                for dx,dy in directions:
                    checkx = dx+row
                    checky = dy+col
                    if 0 <= checkx < n and 0 <= checky < m and (checkx,checky) not in visited:
                        if grid[checkx][checky] == '1':
                            queue.append((checkx,checky))
                            visited.add((checkx,checky))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    res += 1

        return res

