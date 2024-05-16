class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker = {}
        for i in nums:
            if i in checker: return True
            checker[i]=1
        return False
    

#time o(n)
#space o(n)