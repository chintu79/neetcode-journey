class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        answer = []

        for i, word in enumerate(strs):
            w= ''.join(sorted(word))
            data.setdefault(w, []).append(strs[i])

        for value in data.values():
            answer.append(value)

        return answer