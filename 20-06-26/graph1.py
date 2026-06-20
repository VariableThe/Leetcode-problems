class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        has_incoming_edge = [False] * n

        for _, to_node in edges:
            has_incoming_edge[to_node] = True

        return [i for i in range(n) if not has_incoming_edge[i]]
