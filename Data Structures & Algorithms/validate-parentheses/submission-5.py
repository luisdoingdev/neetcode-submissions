class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = {")":"(", "}":"{", ']':"[" }
        stack = []

        for c in s:
            if c not in PAIRS:
                stack.append(c)
            else:
                if not stack or stack[-1] != PAIRS[c]:
                    return False
                stack.pop()

        return len(stack) == 0