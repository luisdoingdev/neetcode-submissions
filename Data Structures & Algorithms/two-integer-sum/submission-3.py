class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = sorted((v, i) for i, v in enumerate(nums))
        l, r = 0, len(pairs) - 1
        while l < r:
            s = pairs[l][0] + pairs[r][0]
            if s == target:
                return sorted([pairs[l][1], pairs[r][1]])
            elif s < target:
                l += 1
            else:
                r -= 1
        
