class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            checker = target - nums[i]
            if checker in res:
                return res[checker], i
            res[nums[i]] = i
        return res