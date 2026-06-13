class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        loop = 0
        while loop != 2:
            for n in nums:
                ans.append(n)
            loop += 1
        
        return ans