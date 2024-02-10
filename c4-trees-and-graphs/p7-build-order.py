"""
[LeetCode]210. Course Schedule II

Problem Statement:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. 
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. 

If it is impossible to finish all courses, return an empty array.

Example:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3] or [0,1,2,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Approach:
The problem can be solved using Topological Sorting of a Directed Graph. 
Each course can be represented as a node, and a prerequisite relationship is a directed edge from one node to another. 
The goal is to find a topological ordering of the nodes (courses) that satisfies the prerequisite conditions.

1. Build a graph from the prerequisites list.
2. Use a queue to keep track of all nodes with no incoming edges (courses with no prerequisites).
3. While the queue is not empty, remove a node and add it to the order list. For each node that was connected to this node, remove the edge and if the node now has no incoming edges, add it to the queue.
4. If the order list has numCourses elements, return the order. Otherwise, return an empty list indicating it is impossible to finish all courses.

Complexity Analysis:
- Time Complexity: O(V + E), where V is the number of courses, and E is the number of prerequisites. This accounts for building the graph and performing the topological sort.
- Space Complexity: O(V + E), for storing the graph and the data structures used for finding the topological order.

"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the graph
        graph = defaultdict(list)
        in_degree = {i: 0 for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        # Find all courses with no prerequisites
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == numCourses else []


# Example usage
if __name__ == "__main__":
    sol = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(sol.findOrder(numCourses, prerequisites))  # Output: [0,1,2,3] or [0,2,1,3]
