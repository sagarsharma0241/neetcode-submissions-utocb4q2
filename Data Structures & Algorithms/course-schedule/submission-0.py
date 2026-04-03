class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {crs: [] for crs in range(numCourses)}
        for crs1,crs2 in prerequisites:
            preReq[crs1].append(crs2)
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            
            if preReq[crs] == []:
                return True

            visitSet.add(crs)
            for preReqCourse in preReq[crs]:
                if not dfs(preReqCourse) : return False
            preReq[crs] = []
            visitSet.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True