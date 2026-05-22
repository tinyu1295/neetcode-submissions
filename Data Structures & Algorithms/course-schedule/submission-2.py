class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        print(preMap)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print("curr", preMap)

        visitSet = set()

        def dfs(node):
            if node in visitSet:
                return False
            if preMap[node] == []:
                return True
            visitSet.add(node)
            for neighbour in preMap[node]:
                if not dfs(neighbour): return False
            visitSet.remove(node)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        
        # return preMap
            

        


        