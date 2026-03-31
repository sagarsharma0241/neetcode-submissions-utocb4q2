class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        res = 0 

        while l <= r :
            if maxL <= maxR:
                
                maxL = max(maxL, height[l])
                res = res + (maxL - height[l])
                l = l + 1
            
            else:
                
                maxR = max(maxR, height[r])
                res = res + (maxR - height[r])
                r = r - 1
        return res


        