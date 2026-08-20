class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n: 
                correct_idx = nums[i] - 1 

                if nums[correct_idx] == nums[i]:
                    break

                nums[correct_idx], nums[i] = nums[i], nums[correct_idx] #[-1,4,3,1]

        for i in range(n): 
            if nums[i] != i+1: 
                return i +1

        return n + 1

    

                

        

        







        
      