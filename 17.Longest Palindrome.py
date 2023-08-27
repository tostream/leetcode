class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        result = {}
        remind = 0
        res=0
        for i in s:
            result[i] = result.get(i,0)+1
        if len(result)<= 1:return len(s)
        for j in result:
            remind += result[j]%2
            res += result[j] - result[j]%2

        if remind> 0:
            res +=  1
        return res

#time=o(n)
#space=o(n)