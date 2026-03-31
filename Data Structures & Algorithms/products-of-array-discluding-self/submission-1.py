class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #start with the prefix arr such that it stores 
        # all the prefix multiples
        # then iterate backwards to multiply postfix multiple


        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *=postfix
            postfix *=nums[i]
        return res
        