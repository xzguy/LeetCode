import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        G = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses

    # below are other solutions
    def build_addacency_list(self, n: int, edegelist: [[int]]) -> [[int]]:
        adj_list = [[] for _ in range(n)]
        for j, i in edegelist:
            adj_list[i].append(j)
        return adj_list

    def canFinish_1(self, numCourses: int, prerequisites: [[int]]) -> bool:
        adj_list = self.build_addacency_list(numCourses, prerequisites)
        visited = set()

        def has_cycle(v: int, stack: [int]):
            if v in visited:
                if v in stack:
                    # This vertex is being processed and it means we have a cycle.
                    return True
                # This vertex is processed so we pass
                return False

            visited.add(v)
            stack.append(v)
            
            for i in adj_list[v]:
                if has_cycle(i, stack):
                    return True
            
            stack.pop()
            return False
        
        for v in range(numCourses):
            if has_cycle(v, []):
                return False
        
        return True


sol = Solution()
numCourses = 4
prerequisites = [[0,1],[3,1],[1,3],[3,2]]
print(sol.canFinish(numCourses, prerequisites))