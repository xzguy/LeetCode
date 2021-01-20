import collections

class Solution:
    # graph indegree method
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        G = [[] for _ in range(numCourses)]
        degree = [0 for _ in range(numCourses)]
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        res = [i for i in range(numCourses) if degree[i] == 0]
        # if variable 'res' appended values during the loop, i will be that values
        for i in res:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    res.append(j)
        if len(res) < numCourses:
            return []
        return res

    # DFS with 3 states: white, gray, black
    def findOrder_1(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        # Create the adjacency list representation of the graph
        adj_list = collections.defaultdict(list)
        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        topological_sorted_order = []
        is_possible = True

        # By default all vertces are white
        color = {k: "white" for k in range(numCourses)}

        def dfs(node: int):
            nonlocal is_possible

            if not is_possible:
                return
            # start the recursion
            color[node] = "gray"

            # traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == "white":
                        dfs(neighbor)
                    elif color[neighbor] == "gray":
                        # an edge to a gray vertex represents a cycle
                        is_possible = False
            
            # recursion ends. Mark it as black
            color[node] = "black"
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            if color[vertex] == "white":
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,1],[3,2],[1,3]]
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses = 3
prerequisites = [[1,0],[2,1]]
print(sol.findOrder(numCourses, prerequisites)) 