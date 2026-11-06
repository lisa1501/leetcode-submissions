class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        # nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]] Output: [8,6,2,4]
        # even_sum = 6
        # [1,0], [-3,1] = 6-2=4 + (-3) =1
        # is not sorted
        # duplicate num in nums  can be
        # -104 <= nums[i] <= 104 can be negative
        # res = []
        # 1. even_sums = get even sum of nums, => add even num from nums
        # 2. loop thru queries, querie = [val, idx] check by idx num of nums ,nums[idx]
        # 3. if nums[idx] is even, even_sums - nums[idx]
        # 4. cur_sum = nums[idx] + val
        # 5. if cur_sum is even, even_sum += cur_sum
        # 6. res append even_sum
        # 7. for done return res
        # nums = [1], queries = [[4,0]]
        # even_sum = 0 
        # []4,0] = nums[0] =>1 is not even, it is odd , cum_sum = 1+4=5 odd
        # time: O(n + m) => O(n) space: O(k) n: len(nums), m:len(queries)
        even_sum = 0 # 6
        for num in nums: 
            if num % 2 == 0:
                even_sum += num
        result = []
        for val, idx in queries: #[-4,0]
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
   
            result.append(even_sum)
       
        return result






        


            

        

        