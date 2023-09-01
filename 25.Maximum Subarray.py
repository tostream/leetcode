
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<1 :return 0
        cur_sum= 0
        result =   nums[0]
        left =0
        right=0
        while left <= right and right <len(nums):
            cur_sum += nums[right]
            result = max(result,cur_sum)
            right+=1
            if cur_sum < 0:
                left = right
                cur_sum= 0
        return result

#time o(n)
#space o(1)