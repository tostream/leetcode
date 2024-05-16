class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker = {}
        if len(s) != len(t): return False
        for i in range(len(s)):
            checker[s[i]] = checker.get(s[i],0)+1
            checker[t[i]] = checker.get(t[i],0)-1
        for j in checker:
            if checker[j] != 0:
                return False

        return True
#time o(n)
#space o(n)
