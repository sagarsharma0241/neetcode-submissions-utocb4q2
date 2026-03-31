class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        

        countTHMap = {}
        windowOverS = {}

        for c in t:
            countTHMap[c] = 1+ countTHMap.get(c,0)
        

        unique_T_vals = len(countTHMap)
        unique_W_vals = 0

        l = 0

        res, resLength = [-1,-1] , float("infinity")

        for r in range(0,len(s)):
            c = s[r]
            windowOverS[c] = 1+ windowOverS.get(c,0)

            if c in countTHMap and countTHMap[c] == windowOverS[c]:
                unique_W_vals +=1
            
            while unique_W_vals == unique_T_vals:
                
                if (r - l + 1 )< resLength:
                    resLength = r - l + 1
                    res = [l,r]
                windowOverS[s[l]] -=1
                if s[l] in countTHMap and countTHMap[s[l]] > windowOverS[s[l]]:
                    unique_W_vals -=1
                l +=1
        l,r = res
        print(res)
        return s[l:r+1] if resLength != float("infinity") else ""




        