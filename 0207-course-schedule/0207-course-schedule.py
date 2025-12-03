class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) #graph = {0: [], 1: [],  2: [], 3: []}
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:  # found a cycle
                return False
            if visited[course] == 2:  # already processed
                return True

            visited[course] = 1  # mark as visiting

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visited[course] = 2  # mark as fully visited
            return True
        
        for c in range(numCourses):
            if visited[c] == 0:  # not yet visited
                if not dfs(c):
                    return False

        return True