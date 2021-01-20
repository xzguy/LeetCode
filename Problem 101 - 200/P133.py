import collections
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

'''
The difference between this graph traverse and tree
traverse is that there may be loops in the graph, so
take a record of traversed nodes.
'''
class Solution:
    # graph DFS iteratively
    def cloneGraph_1(self, node: Node) -> Node:
        if not node:
            return node
        # dictionary, key is original node, value is copy node
        m = {node: Node(node.val)}
        stack = [node]
        while stack:
            n = stack.pop()
            for neigh in n.neighbors:
                if neigh not in m:
                    stack.append(neigh)
                    m[neigh] = Node(neigh.val)
                # the graph edge should be copied
                # no matter the node is traversed or not
                m[n].neighbors.append(m[neigh])
        return m[node]

    # graph BFS
    def cloneGraph_2(self, node: Node) -> Node:
        if not node:
            return node
        m = {node: Node(node.val)}
        queue = collections.deque([node])
        while queue:
            n = queue.popleft()
            for neigh in n.neighbors:
                if neigh not in m:
                    queue.append(neigh)
                    m[neigh] = Node(neigh.val)
                # build the graph edge
                m[n].neighbors.append(m[neigh])
        return m[node]

    # graph DFS recursively
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        m = {node: Node(node.val)}
        self.dfs(node, m)
        return m[node]

    def dfs(self, node, m):
        for neigh in node.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
                self.dfs(neigh, m)
            m[node].neighbors.append(m[neigh])