class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        final = []
        sum_pre = 1
        sum_suf = 1
        j = len(nums)-1

        if len(nums) > 0:
            prefix.append(1)
            suffix.append(1)

        for i in range(len(nums)-1):
            sum_pre = sum_pre * nums[i]
            prefix.append(sum_pre)

        while j >= 1:
            sum_suf = sum_suf * nums[j]
            suffix.append(sum_suf)
            j -= 1

                
        suffix.reverse()
        for s in range(len(nums)):
            final.append(suffix[s] * prefix[s])

        return final