class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        path = []
        res = []

        def twoSum(start, target):
            l = start 
            r = len(nums) - 1

            while l < r:
                cur_sum = nums[l] + nums[r]
                if  cur_sum < target:
                    l += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    res.append(path + [nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        def kSum(k, start, target):
            if k == 2:
                twoSum(start, target)
                return 

            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                kSum(k-1, i+1, target-nums[i])
                path.pop()

        kSum(3, 0, 0)
        return res