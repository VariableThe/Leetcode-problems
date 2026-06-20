class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j


class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        dsu = DSU(n)
        result = []

        for u, v in requests:
            root_u, root_v = dsu.find(u), dsu.find(v)

            possible = True
            for x, y in restrictions:
                root_x, root_y = dsu.find(x), dsu.find(y)
                if (root_u == root_x and root_v == root_y) or (
                    root_u == root_y and root_v == root_x
                ):
                    possible = False
                    break

            if possible:
                dsu.union(u, v)
                result.append(True)
            else:
                result.append(False)

        return result
