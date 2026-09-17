# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}
        def build_parent(node,parent):
            if not node:
                return 
            parent_map[node] = parent
            build_parent(node.left,node)
            build_parent(node.right,node)
        build_parent(root,None)
        queue = deque([target])
        visited = {target}
        distance = 0
        while queue:
            if distance ==k:
                values= []
                for node in queue:
                    values.append(node.val)
                return values
            for i in range(len(queue)):
                node = queue.popleft()
                neighbors = [
                    node.left,
                    node.right,
                    parent_map[node]
                ]
                for neighbor in neighbors:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance+=1
        return []