class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadySeen = set()
        for elem in nums:
            if elem in alreadySeen:
                return True;
            alreadySeen.add(elem);
        return False