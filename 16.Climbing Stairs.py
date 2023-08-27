class Solution:
    def climbStairs(self, n: int) -> int:
        checker ={0:1,1:1}
        def dp(n):
            if n not in checker:
                checker[n] = dp(n-1) + dp(n-2)
            return checker[n]
        return dp(n)
    
#time = o(n)
#space = o(n)