class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
                
            stack.append(num)
        res = []
        for num in nums1:
            if num in next_greater:
                res.append(next_greater[num])
            else:
                res.append(-1)

        return res

        