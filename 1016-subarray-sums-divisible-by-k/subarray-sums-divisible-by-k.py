class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        seen = {0:1}
        prefix_sum = 0

        for i in range(len(nums)):
            num = nums[i]
            prefix_sum += num
            remain = prefix_sum % k

            if remain in seen:
                res += seen[remain]
                
            seen[remain] = seen.get(remain, 0) + 1
       
        return res
        