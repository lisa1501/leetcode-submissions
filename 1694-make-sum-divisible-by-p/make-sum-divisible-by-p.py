class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        
        if target == 0:
            return 0

        prefix = 0
        seen = {0:-1}
        ans = len(nums)
        length = 0

        for i in range(len(nums)):
            num = nums[i]
            prefix = (prefix + num) % p
            needed = (prefix - target) % p
            # i=0, num=3, prefix=3, needed=5, seen={0:-1, 3:0}
            # i=1, num=1, prefix=4, needed=0, 
                # length = 1 - (-1)=2, ans = 2, seen={0:-1, 3:0, 4:1}
            # i=2, num=4, prefix=2, needed=4, 
                # length = 2 - (-1) = 1, ans = 1, seen={0:-1, 3:0, 4:1, 2:2}
            # i=3, num=2, prefix=4, needed=0 
                # length = 3 - (-1) = 4, ans = 1, 

            if needed in seen:
                lenght = i - seen[needed]
                ans = min(ans, lenght)

            seen[prefix] = i 


        if ans == len(nums):
            return -1
        return ans
        