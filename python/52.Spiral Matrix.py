class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        db = len(matrix) -1
        rb = len(matrix[0])-1
        ub = 0
        lb = 0
        #right = plus y
        #down = plus x
        #left = minus y
        #up = minux x
        directions = [0,1]
        res =[]
        i,j = 0,0
        while len(res) < (m*n):
            res.append(matrix[i][j])
            if i + directions[0] > db: 
                directions[0] = 0
                directions[1] = -1
                rb -= 1
            elif i + directions[0] < ub: 
                directions[0] = 0
                directions[1] = 1
                lb += 1
            elif j + directions[1] > rb:
                ub += 1
                directions[0] = 1
                directions[1] = 0
            elif j + directions[1] < lb:
                db -= 1
                directions[0] = -1
                directions[1] = 0
            i = i + directions[0] 
            j = j + directions[1]

        return res

#time: o(m*n)
#space: o(m*n)