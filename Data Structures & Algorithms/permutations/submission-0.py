class Solution:
    def backtrack(self, n, curr, permutations, nums, used):
        if len(curr) == n:
            return curr[:]
        
        for i in range(n):
            if used[i]:
                continue
            curr.append(nums[i])
            used[i] = True
            order = self.backtrack(n, curr, permutations, nums, used)

            if (order is not None):
                permutations.append(order)
                
            curr.remove(nums[i])
            used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.backtrack(len(nums), [], permutations, nums, [False]*len(nums))
        return permutations