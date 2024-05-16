class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        k = 0 
        while n > k:
            m = k+ ((n-k)//2)
            if nums[m] == target:
                return m
            if nums[m] < target:
                k = m +1
            else:
                n = m
        return -1

