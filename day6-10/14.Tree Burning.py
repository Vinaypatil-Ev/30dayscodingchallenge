import collections
class Solution:
    def minTime(self, root,target):
        # code here
        graph = collections.defaultdict(list)
        def dfs(root):
            if root is None:
                return
            if root.left:
                graph[root.data].append(root.left.data)
                graph[root.left.data].append(root.data)
                dfs(root.left)
            if root.right:
                graph[root.data].append(root.right.data)
                graph[root.right.data].append(root.data)
                dfs(root.right)
        dfs(root)
        q = collections.deque()
        q.append(target)
        vis = set()
        vis.add(target)
        time = -1
        while q:
            for _ in range(len(q)):
                
                node = q.popleft()
                vis.add(node)
                for adj in graph[node]:
                    if adj not in vis:
                        q.append(adj)
            time += 1
        return time
        