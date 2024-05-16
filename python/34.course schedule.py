class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        checker = { i:[] for i in range(numCourses)}
        checked = set()
        def dfs(course):
            if course in checked:return False
            temp = checker[course]
            if len(temp) <1: return True
            if not temp: return True
            checked.add(course)
            for i in temp:
                if not dfs(i):return False
            checked.remove(course)
            checker[course] = [] # copy from neetcode, i didn't figure out this part
            return True

        for course,prer in prerequisites:
            checker[course].append(prer)
        
        for i in range(numCourses):
            result = dfs(i)
            if not result: return result
        return True