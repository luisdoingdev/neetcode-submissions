from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = Counter(nums)
        return max(majority_element, key=majority_element.get)

        