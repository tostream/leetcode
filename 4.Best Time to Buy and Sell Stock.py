class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        i = 0
        j = 1
        while i < len(prices) and j <len(prices):
            if prices[j] < prices[i]:
                i=j
            else :
                result = max(result,prices[j] - prices[i])
            j+=1
        return result