class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for a,elem in enumerate(nums):
            if (a > 0 and elem == nums[a-1]):
                continue
            l = a + 1
            r = len(nums) - 1
            while l < r:
                if ((elem + nums[l] + nums[r]) > 0):
                    r = r -1
                elif((elem + nums[l]+ nums[r]) < 0):
                    l = l + 1
                else:
                    res.append([elem, nums[l], nums[r]])
                    l = l + 1
                    while(nums[l] == nums[l -1] and l < r ):
                        l = l + 1
        return res

        