class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]


class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        dsu = DSU(max_num)

        for num in nums:
            d = 2
            temp = num
            while d * d <= temp:
                if temp % d == 0:
                    dsu.union(num, d)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                dsu.union(num, temp)

        count = {}
        max_size = 0
        for num in nums:
            root = dsu.find(num)
            count[root] = count.get(root, 0) + 1
            max_size = max(max_size, count[root])

        return max_size
