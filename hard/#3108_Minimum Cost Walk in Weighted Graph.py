class Solution:
    def get_component_cost(self, source, adjList, visited, components, component_id):
        nodes_queue = deque()
        component_cost = -1
        # *************************
        nodes_queue.append(source)
        visited[source] = True

        # BFS
        while nodes_queue:
            node = nodes_queue.popleft()
            components[node] = component_id
            
            # go through all the adjacent nodes
            for neighbor, weight in adjList[node]:
                # update the component cost (bitwise AND)
                component_cost &= weight

                if visited[neighbor]:
                    continue
                # if the neighbor hasn't been visited, mark it as visited and add to queue
                visited[neighbor] = True
                nodes_queue.append(neighbor)
        return component_cost

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Disjoint-set
        # create a adjacency list for the graph
        adjList = [[] for _ in range(n)]
        for edge in edges:
            adjList[edge[0]].append((edge[1], edge[2]))
            adjList[edge[1]].append((edge[0], edge[2]))

        visited = [False] * n
        components = [0] * n
        component_cost = []
        component_id = 0
        
        # BFS for each unvisited node to indentify components and calculate their costs
        for node in range(n):
            if not visited[node]:
                component_cost.append(self.get_component_cost(node, adjList, visited, components, component_id))
                component_id += 1
        
        result = []
        for q in query:
            start, end = q
            if components[start] == components[end]:
                result.append(component_cost[components[start]])
            else:
                result.append(-1)
        return result

    # ref: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/editorial
