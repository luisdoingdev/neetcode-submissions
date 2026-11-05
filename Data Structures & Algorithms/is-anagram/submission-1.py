class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # https://docs.python.org/3/library/collections.html#counter-objects 
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

        