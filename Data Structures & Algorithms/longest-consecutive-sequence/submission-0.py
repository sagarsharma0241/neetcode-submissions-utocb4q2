class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        input_set = set(nums)

        longest = 0

        for elem in nums:
            largest_so_far = 0
            while ((elem + largest_so_far) in input_set ):
                largest_so_far +=1
            longest = max(largest_so_far, longest)
        
        return longest