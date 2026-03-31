class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            d.setdefault(num, []).append(nums[i])
            
        sorted_items = sorted(d.items(), key=lambda x: len(x[1]), reverse=True)
        sorted_dict = dict(sorted_items)

        keys = list(sorted_dict.keys())
        ans = keys[:k]
        

        return ans