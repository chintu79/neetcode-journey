class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        substr = set()
        max_len = 0

        while right < len(s):

            print(substr)
            
            while right < len(s) and s[right] in substr:
                substr.discard(s[left])
                left += 1
                    
            substr.add(s[right])
            max_len = max(max_len,(right - left + 1))

            right += 1
        return max_len
