class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result  ={}
        for i in nums:
            result[i] = result.get(i,0)+1
        max_count =0
        index= -1
        for j in result:
            if result[j] > max_count:
                max_count = result[j]
                index = j
        return index
#time o(n)
#space o(n)