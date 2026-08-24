class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        for amt in range(0, amount+1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], dp[amt-coin]+1)
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
