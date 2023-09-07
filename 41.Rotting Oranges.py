class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_list = set()
        n= len(grid)
        m=len(grid[0])
        rotten_list = []
        res = 0 
        mins=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_list.add((i,j))
                if grid[i][j] == 2:
                    rotten_list.append((i,j,mins))
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while rotten_list:
            rotten = False
            rx,ry,mins = rotten_list.pop(0)
            mins+=1
            for dx,dy in directions:
                checkerx = rx+dx 
                checkery = ry+dy
                if 0 <= checkerx < n and 0<= checkery < m and grid[checkerx][checkery] == 1 and \
                (checkerx,checkery) in fresh_list:
                    rotten = True 
                    grid[checkerx][checkery] = 2
                    fresh_list.remove((checkerx,checkery))
                    rotten_list.append((checkerx,checkery,mins))
                if rotten: res = mins


        if len(fresh_list)>0:return -1

        return res

#time: o(number of fresh orange)
#space: o(number of fresh orange)