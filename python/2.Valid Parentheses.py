class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        answer ={
            '}':'{',
            ']':'[',
            ')':'(',
             }
        for i in s:
            if len(res)>0 and res[-1] == answer.get(i,0):
                res.pop()
            else:
                res.append(i)
        
        return len(res) == 0