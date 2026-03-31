class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False

        t_sort = "".join(sorted(t))
        s_sort = "".join(sorted(s))

        if s_sort == t_sort:
            return True
        else:
            return False


