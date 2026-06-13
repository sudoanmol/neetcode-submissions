class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            for k, v in seen.items():
                if n + v == target:
                    return [k,i]
                    
            seen[i] = n