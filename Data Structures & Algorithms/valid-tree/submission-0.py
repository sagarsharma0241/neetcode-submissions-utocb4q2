class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map_nodes = {c : [] for c in range(n)}

        for node1, node2 in edges:
            map_nodes[node1].append(node2)
            map_nodes[node2].append(node1)
        
        visit = set()
        prev = -1

        def dfs(curr, prev):
            if curr in visit:
                return False
            visit.add(curr)

            for next_node in map_nodes[curr]:
                if next_node == prev: continue

                if dfs(next_node, curr) == False : 
                    return False
            return True
        result = dfs(0,-1)
        if len(visit) == n:
            return result
        else:
            return False
