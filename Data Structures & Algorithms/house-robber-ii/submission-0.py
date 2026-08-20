class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp_end = [0]*n
        dp[0] = nums[0]
        if (n > 1):
            dp[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        if (n > 1):
            dp_end[0] = nums[1]
        if (n > 2):
            dp_end[1] = max(nums[1], nums[2])
        for i in range(3, n):
            dp_end[i-1] = max(nums[i] + dp_end[i-3], dp_end[i-2])
        return max(dp_end[n-2], dp[n-2])