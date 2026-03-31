class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(s):
                res.append(subset.copy())
                return 
            
            for j in range(i, len(s)):
                if self.isPali(i,j,s):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop() 
        dfs(0)      
        return res
    def isPali(self, i,j, s):
        while i <=j:
            if s[i] != s[j]:
                return False
            j = j -1
            i = i+1
        return True

 



        