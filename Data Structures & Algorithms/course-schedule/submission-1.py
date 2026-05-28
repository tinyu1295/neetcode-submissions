class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqDic = {}

        for course, req in prerequisites:
            if course == req:
                return False
            if not req in reqDic:
                reqDic[course] = req
            elif req in reqDic:
                return False
        return True


        