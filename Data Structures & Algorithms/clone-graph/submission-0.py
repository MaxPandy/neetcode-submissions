"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node

        stack=[node]
        visited={node:Node(node.val)}

        while stack:
            curr=stack.pop()
            for i in curr.neighbors:
                if i not in visited:
                    visited[i]=Node(i.val)
                    stack.append(i)
                visited[curr].neighbors.append(visited[i])
        return visited[node]
            