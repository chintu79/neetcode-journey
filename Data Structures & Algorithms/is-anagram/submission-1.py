class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if len(s) != len(t):
            return False

        s_count = []
        t_count = []

        for ch in s:
            s_count.append(ord(ch))

        for c in t:
            t_count.append(ord(c))

        s_count.sort()
        t_count.sort()

        for i in range(len(s_count)):
            if s_count[i] != t_count[i]:
                return False
        return True


