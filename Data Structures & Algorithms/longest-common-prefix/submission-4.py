class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        template = strs[0]
        for i in range(len(template)):
            for word in strs:
                if i >= len(word) or word[i] != template[i]:
                    return template[:i]
        return template
            