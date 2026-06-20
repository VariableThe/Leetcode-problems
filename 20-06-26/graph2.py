class Solution(object):
    def isPossible(self, n, edges):
        adj = [set() for _ in range(n + 1)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        odd_nodes = [i for i in range(1, n + 1) if len(adj[i]) % 2 != 0]
        count = len(odd_nodes)

        if count == 0:
            return True
        if count > 4:
            return False

        def can_add(u, v):
            return v not in adj[u]

        if count == 2:
            u, v = odd_nodes[0], odd_nodes[1]
            if can_add(u, v):
                return True
            for i in range(1, n + 1):
                if can_add(u, i) and can_add(i, v):
                    return True
            return False

        if count == 4:
            a, b, c, d = odd_nodes
            if (
                (can_add(a, b) and can_add(c, d))
                or (can_add(a, c) and can_add(b, d))
                or (can_add(a, d) and can_add(b, c))
            ):
                return True
            return False

        return False
