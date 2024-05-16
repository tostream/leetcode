from typing import List
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = {}
        def dfs(amount):
            if amount == 0: return 0
            if amount <0 :return -1
            min_cost = math.inf
            if amount in visited:
                return visited[amount]
            for i in coins:
                res = dfs(amount-i)
                print(f"cp: result = {res}, amount: {amount} , coin:{i}, {min_cost}")
                if res !=-1:
                    min_cost =min(min_cost,res+1)
            visited[amount] = -1 if min_cost == math.inf else min_cost
            return visited[amount]

        result = dfs(amount)
        return result

temp = Solution()
temp.coinChange([1,2,3],6)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount +1]* (amount+1)
        dp[0]=0
        for a in range(1,amount+1):
            for c in coins:
                if a -c >=0:
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return -1 if dp[amount] == (amount+1) else dp[amount] 