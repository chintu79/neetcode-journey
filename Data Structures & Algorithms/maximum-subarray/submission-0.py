class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_num = nums[0]
        max_num = nums[0]

        for i in range(1, len(nums)):
            curr_num = max(nums[i], curr_num + nums[i])
            max_num = max(max_num, curr_num)
        return max_num
            