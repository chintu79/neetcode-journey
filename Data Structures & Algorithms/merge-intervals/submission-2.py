class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        p = 0
        c = 1

        intervals.sort()

        while c < len(intervals):
            curr = intervals.pop(c)
            prev = intervals.pop(p)

            maxi = max(curr[1], prev[1])
            if prev[1] >= curr[0]:
                intervals.append([prev[0], maxi])
            else:
                intervals.append(prev)
                intervals.append(curr)
                p += 1
                c += 1
            intervals.sort()     

        return intervals