class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for curr in intervals[1:]:
            prev = merged[-1]
            
            if curr[0] <= prev[1]:
                prev[1] = max(curr[1], prev[1])
            else:
                merged.append(curr)
        return merged