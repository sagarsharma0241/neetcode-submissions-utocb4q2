class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for idx, elem in enumerate(nums):
            diff = target - elem
            if diff in seen_map: 
                return [seen_map[diff], idx]
            seen_map[elem] = idx
        return 