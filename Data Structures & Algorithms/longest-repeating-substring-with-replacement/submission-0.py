class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxL = 0

        for r in range(0, len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            while (r - l + 1) - max(count.values()) >k:
                count[s[l]] = count[s[l]] - 1
                l = l + 1

            maxL = max(maxL, (r - l + 1))
        
        return maxL

        