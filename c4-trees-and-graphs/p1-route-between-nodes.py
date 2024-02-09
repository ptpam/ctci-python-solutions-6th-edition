"""
[LeetCode] 1971. Find if Path Exists in Graph (Easy) 

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. 
Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Approach:
The problem can be solved using a graph traversal algorithm like Breadth-First Search (BFS). 
We first construct the graph as an adjacency list, then use BFS to explore the graph from the source vertex, marking vertices as visited. 
If we can reach the destination vertex, return true; otherwise, if the traversal completes without reaching the destination, return false.

Complexity Analysis:
- Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges. This accounts for building the graph and traversing it.
- Space Complexity: O(V + E) for the adjacency list representation of the graph and additional O(V) space for the BFS queue and visited set, leading to O(V + E) total space complexity.

Solution:
"""

from typing import List
from collections import deque


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        # Build the graph using an adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize a queue for BFS and a set to keep track of visited vertices
        queue = deque([source])
        visited = set([source])

        # Perform BFS
        while queue:
            vertex = queue.popleft()
            if vertex == destination:
                return True
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        # If BFS completes without finding the destination, no path exists
        return False


# Example usage
if __name__ == "__main__":
    sol = Solution()
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    print(sol.validPath(n, edges, source, destination))  # Output: true
