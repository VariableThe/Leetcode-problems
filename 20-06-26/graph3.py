class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        graph = [[] for _ in range(len(values))]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        visited_count = [0] * len(values)
        self.max_quality = 0

        def dfs(u, current_time, current_quality):
            if visited_count[u] == 0:
                current_quality += values[u]
            visited_count[u] += 1

            if u == 0:
                self.max_quality = max(self.max_quality, current_quality)

            for v, t in graph[u]:
                if current_time + t <= maxTime:
                    dfs(v, current_time + t, current_quality)

            visited_count[u] -= 1

        dfs(0, 0, 0)
        return self.max_quality
