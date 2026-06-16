class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicates for i
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                
                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    # skip duplicates for l
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif sum < 0:
                    l+=1
                else:
                    r-=1

        return res