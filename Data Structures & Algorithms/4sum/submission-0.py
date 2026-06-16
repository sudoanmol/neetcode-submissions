class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # skip i duplicates
                continue

            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:  # skip j duplicates
                    continue

                l, r = j + 1, len(nums) - 1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                
                    if sum == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        # skip duplicates for l
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                    elif sum < target:
                        l+=1
                    else:
                        r-=1

        return res