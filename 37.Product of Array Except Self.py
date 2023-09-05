class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1]*(length)
        desc_rd =  [1]*(length) 
        asc_rd =  [1]*(length)
        for i in range(1,length):
            asc_rd[i] =asc_rd[i-1]*nums[i-1]
        for i in reversed(range(length-1)):
            print(f"{desc_rd[i]} , {desc_rd[i+1]}, {nums[i+1]}")
            desc_rd[i] =desc_rd[i+1]*nums[i+1]
        for i in range(length):
            res[i]=asc_rd[i]*desc_rd[i]
        return res