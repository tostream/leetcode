class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            m = l+(r-l) // 2
            print(f"{m} , {l} - {r}")
            if nums[m] == target:return m
            elif nums[m] < target :
                if nums[r] < target:
                    l = m+1
                else:
                    r = m
            elif nums[m] > target:
                if nums[l] > target:
                    l = m+1
                else:
                    r = m


        return -1
#i can't figure out

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:return m
            elif nums[l] <=nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1    
                else:
                    l = m + 1   

        return -1
# this is come from neetcode explanation