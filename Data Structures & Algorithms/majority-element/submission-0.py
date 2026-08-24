class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele = nums[0]
        n = len(nums)
        for i in range(n):
            if nums[i] == ele:
                count += 1
            else:
                count -= 1
                if count == 0:
                    ele = nums[i]
                    count = 1
        return ele