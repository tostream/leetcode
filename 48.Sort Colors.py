class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        p=0
        c=0
        while c< len(nums)-1:
            if nums[c] >  nums[c+1]:
                nums[c],nums[c+1] = nums[c+1],nums[c]
            p = c
            while p >0:
                p-=1
                if nums[p] >  nums[p+1]:
                    nums[p],nums[p+1] = nums[p+1],nums[p]
            c+=1

#time: o(n**2)
#space: o(1)