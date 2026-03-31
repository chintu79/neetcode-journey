class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        length = len(heights)

        left = 0
        right = length -1

        while True:
    
            if left > right:
                break
            else:
                width = abs(left - right)
                height = min(heights[left], heights[right])
                area = width * height
                maximum = max(maximum, area)
                if heights[left] > heights[right]:
                    right -= 1
                else:
                    left += 1
        return maximum
            
