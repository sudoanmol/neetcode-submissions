class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0

        while l < len(numbers):
            for i in range(1, len(numbers)):
                if numbers[l] + numbers[i] == target:
                    return [numbers[l], numbers[i]]
            l+=1