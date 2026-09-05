class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # nums = [3,1,4,2], p = 6
        # prefix sum
        # return smallest =>  min val , min(len(nums), subarr len)
        # prefix sum, hm store prefxi sum: cur num idx, lenght  =0 
        # {0:1, 3:0, 4:1}
        # calculate sum of nums, module p, target, 10%6 =4
        # if reminder is 0 return 0
        # for loop on nums, 
        #  increase prefix sum by cur num, 
        # prefix sum % p, 
        # (prefix sum - target) % p in hm or 
        # if in hm :
        # cur len is cur idx - what we see in hm , the previout idx num
        # updated smallest min of cur len  and len of nums
        # hm[prefixsum] = cur idx
        # updated smallest is len of nums reutrn -1
        # return updated smallest

        # time: O(n), Space:O(n)
        # [3,1,4,2], p = 6

        total = sum(nums) #10
        target = total % p #4
        if target == 0:
            return 0

        prefix_sum = 0
        seen = {0: -1}
        ans = len(nums)
        length = 0

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            needed = (prefix_sum - target) % p

            if needed in seen:
                length = i - seen[needed]
                ans = min(ans, length)

            seen[prefix_sum] = i

        if ans == len(nums):
            return -1 
    
        return ans






        