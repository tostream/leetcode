class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            checker = {}
            for j in range(i+1,len(nums)):
                temp = 0 - nums[i]-nums[j]
                if temp in checker:
                    result.append(tuple(sorted([nums[i],checker[temp], nums[j]])))
                checker[nums[j]] = nums[j]
        
        return set(result)
    
#time= o(n square)
#space = o(n)