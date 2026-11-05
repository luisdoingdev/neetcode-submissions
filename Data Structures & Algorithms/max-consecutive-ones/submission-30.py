class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       best = 0
       current = 0
       for num in nums:
            if num == 1: 
                current = current + 1
                if current > best:
                    best = current
            else:
                current = 0
       return best
           


        
                    


        