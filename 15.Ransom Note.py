class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        checker ={}
        for i in magazine:
            checker[i]=checker.get(i,0) + 1
        for i in ransomNote:
            if i  not in checker:
                return False
            if checker[i] < 1:
                return False
            
            checker[i]-=1
        return True