class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = { c : [] for c in range(numCourses)}

        for crs,pre in prerequisites:
            preReq[crs].append(pre)

        visit, cycle = set(), set()
        output = []
        def dfs(crs):

            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)

            for pre in preReq[crs]:
                if dfs(pre) == False:
                    return False
            output.append(crs)
            cycle.remove(crs)
            visit.add(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output   

