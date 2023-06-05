"""
Reorder Routes to Make All Paths Lead to the City Zero
Difficulty: Medium

> https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

Notes:
    - Beats 7% of time submissions
"""


from typing import List, Dict


class Node:
    def __init__(self, name: int) -> None:
        self.name = name
        self.parents: List["Node"] = []
        self.children: List["Node"] = []

class Solution:
    def recurse_down(self, node: Node, from_node: int) -> int:
        t = 0
        for child in node.children:
            if child.name != from_node:
                t += 1 + self.recurse_down(child, node.name)
        for parent in node.parents:
            if parent.name != from_node:
                t += self.recurse_down(parent, node.name)
        return t

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        nodes: Dict[int, Node] = {i: Node(i) for i in range(n)}

        # first build the tree
        for name, connection in connections:
            nodes[name].children.append(nodes[connection])
            nodes[connection].parents.append(nodes[name])

        return self.recurse_down(nodes[0], 0)

    
if __name__ == "__main__":
    print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])) # 3   
    print(Solution().minReorder(5, [[1,0],[1,2],[3,2],[3,4]])) # 2
    

